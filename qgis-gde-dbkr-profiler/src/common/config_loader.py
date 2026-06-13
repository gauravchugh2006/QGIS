"""Load YAML config files so runtime settings stay outside the code."""

import os
from pathlib import Path

import yaml


PROJECT_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_CONFIG_PATH = PROJECT_ROOT / "config" / "settings.yaml"
DEFAULT_TOOL_SELECTION_PATH = PROJECT_ROOT / "config" / "tool_selection.yaml"


def load_yaml_file(path: Path | str) -> dict:
    """Read a YAML file and return a dict used by the rest of the project."""
    file_path = Path(path)
    with file_path.open("r", encoding="utf-8") as handle:
        data = yaml.safe_load(handle) or {}
    return data


def load_settings(path: Path | str = DEFAULT_CONFIG_PATH) -> dict:
    """Load the main runtime settings for profiling and database access."""
    return apply_environment_overrides(load_yaml_file(path))


def load_tool_selection(path: Path | str = DEFAULT_TOOL_SELECTION_PATH) -> dict:
    """Load the approved tool list used for documentation and governance."""
    return load_yaml_file(path)


def apply_environment_overrides(settings: dict) -> dict:
    """Override YAML settings from environment variables for local or server runs."""
    project = settings.setdefault("project", {})
    profiling = settings.setdefault("profiling", {})
    database = settings.setdefault("database", {})

    project["environment"] = os.getenv("APP_ENV", project.get("environment", "local"))
    project["output_dir"] = os.getenv("OUTPUT_DIR", project.get("output_dir", "reports"))

    profiling["top_n_functions"] = int(
        os.getenv("TOP_N_FUNCTIONS", profiling.get("top_n_functions", 30))
    )
    profiling["enable_cpu_profile"] = _get_bool_env(
        "ENABLE_CPU_PROFILE", profiling.get("enable_cpu_profile", True)
    )
    profiling["enable_elapsed_time"] = _get_bool_env(
        "ENABLE_ELAPSED_TIME", profiling.get("enable_elapsed_time", True)
    )
    profiling["enable_memory_check"] = _get_bool_env(
        "ENABLE_MEMORY_CHECK", profiling.get("enable_memory_check", True)
    )
    profiling["enable_database_profile"] = _get_bool_env(
        "ENABLE_DATABASE_PROFILE", profiling.get("enable_database_profile", True)
    )
    profiling["memory_leak_iterations"] = int(
        os.getenv("MEMORY_LEAK_ITERATIONS", profiling.get("memory_leak_iterations", 3))
    )

    database["host"] = os.getenv("DB_HOST", database.get("host", "localhost"))
    database["port"] = int(os.getenv("DB_PORT", database.get("port", 5432)))
    database["database"] = os.getenv("DB_NAME", database.get("database", "dbkr"))
    database["user"] = os.getenv("DB_USER", database.get("user", "postgres"))
    database["password"] = os.getenv("DB_PASSWORD", database.get("password", "postgres"))
    database["test_query"] = os.getenv("DB_TEST_QUERY", database.get("test_query", "SELECT 1"))

    return settings


def _get_bool_env(name: str, default: bool) -> bool:
    """Parse boolean env vars consistently across local and deployed environments."""
    raw_value = os.getenv(name)
    if raw_value is None:
        return default

    return raw_value.strip().lower() in {"1", "true", "yes", "on"}
