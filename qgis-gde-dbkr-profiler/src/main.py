"""Run the full profiling workflow from config load to final summary output."""

from pathlib import Path

from common.config_loader import PROJECT_ROOT, load_settings
from common.logger import get_logger
from common.report_writer import write_json_report, write_text_report
from dbkr.postgres_query_profiler import profile_postgres_query
from dbkr.profile_dbkr_backend import profile_dbkr_backend_task
from dbkr.profile_dbkr_frontend import profile_dbkr_frontend_task
from gde.profile_gde_backend import profile_gde_backend_task
from gde.profile_gde_frontend import profile_gde_frontend_task
from profiling.cpu_profiler import run_cpu_profile
from profiling.memory_leak_checker import check_memory_growth
from profiling.summary_analyzer import build_summary
from qgis_native.profile_qgis_native_functions import profile_qgis_native_function
from reports.final_report_builder import build_final_report


logger = get_logger(__name__)


def run_database_profile_if_available(config: dict) -> tuple[bool, str]:
    """Attempt database profiling and skip cleanly when PostgreSQL is unavailable."""
    if not config.get("profiling", {}).get("enable_database_profile", False):
        return False, "Database profiling disabled in configuration."

    query = config.get("database", {}).get("test_query", "SELECT 1")
    output_path = PROJECT_ROOT / "reports" / "database" / "postgres_explain_analyze.txt"

    try:
        result = profile_postgres_query(query, config["database"])
        write_text_report(output_path, "\n".join(row[0] for row in result))
        return True, f"Database profile saved to {output_path}"
    except Exception as exc:  # pragma: no cover - depends on local DB availability
        return False, f"Database profile skipped: {exc}"


def run_all_profiles():
    """Orchestrate all profiling steps and return a small execution summary."""
    config = load_settings()
    output_root = PROJECT_ROOT / config["project"]["output_dir"]
    top_n = config["profiling"].get("top_n_functions", 30)

    logger.info("Starting full profiling execution...")

    run_cpu_profile(
        profile_gde_frontend_task,
        output_root / "gde" / "gde_frontend_cpu_report.txt",
        top_n=top_n,
    )
    run_cpu_profile(
        profile_gde_backend_task,
        output_root / "gde" / "gde_backend_cpu_report.txt",
        top_n=top_n,
    )
    run_cpu_profile(
        profile_qgis_native_function,
        output_root / "qgis_native" / "qgis_native_cpu_report.txt",
        top_n=top_n,
    )
    run_cpu_profile(
        profile_dbkr_frontend_task,
        output_root / "dbkr" / "dbkr_frontend_cpu_report.txt",
        top_n=top_n,
    )
    run_cpu_profile(
        profile_dbkr_backend_task,
        output_root / "dbkr" / "dbkr_backend_cpu_report.txt",
        top_n=top_n,
    )

    memory_results = check_memory_growth(
        profile_gde_frontend_task,
        iterations=config["profiling"].get("memory_leak_iterations", 3),
    )
    memory_summary = build_summary("gde_frontend_memory_growth", memory_results)
    write_json_report(output_root / "memory" / "gde_memory_summary.json", memory_summary)

    db_ok, db_message = run_database_profile_if_available(config)

    final_report_path = build_final_report(
        output_root / "final" / "profiling_summary.md",
        {
            "Execution": "CPU, elapsed-time, and memory-growth profiling completed.",
            "Memory": (
                f"Samples: {memory_summary['samples']}, growth: "
                f"{memory_summary['growth']:.2f} MB."
            ),
            "Database": db_message,
        },
    )

    logger.info("Profiling completed.")

    return {
        "memory_summary": memory_summary,
        "database_profile_completed": db_ok,
        "final_report": str(final_report_path),
    }


if __name__ == "__main__":
    run_all_profiles()
