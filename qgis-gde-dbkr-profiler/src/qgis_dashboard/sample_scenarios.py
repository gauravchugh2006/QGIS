"""Provide client-demo scenarios for the QGIS profiling dashboard UI."""

from datetime import datetime


DEFAULT_LOG_PATH = r"C:\Users\Public\Documents\GDE\LOG\Log_20260613150000.txt"

CHECK_LABELS = [
    "Job Status Check",
    "GD Layer Loading",
    "DBKR Layer Loading",
    "CBB Layer Loading",
    "IVP - Last Modification Check",
    "ZOM Workzone Polygon Check",
]


SCENARIOS = {
    "success": {
        "title": "All systems healthy",
        "job_name": "GD-2026-001 / Fiber Expansion",
        "execution_mode": "Client demo - success path",
        "log_path": DEFAULT_LOG_PATH,
        "checks": {
            "Job Status Check": "100%",
            "GD Layer Loading": "100%",
            "DBKR Layer Loading": "100%",
            "CBB Layer Loading": "100%",
            "IVP - Last Modification Check": "100%",
            "ZOM Workzone Polygon Check": "100%",
        },
        "overall": "100%",
        "logs": [
            "Info: Job status validated successfully",
            "Info: GD layers loaded successfully",
            "Info: DBKR PostgreSQL layers loaded successfully",
            "Info: CBB background layers loaded successfully",
            "Info: IVP last modification date verified",
            "Info: ZOM workzone polygon found",
            "Info: Process completed",
        ],
    },
    "ivp_failed": {
        "title": "Stale IVP data detected",
        "job_name": "GD-2026-014 / Utility Refresh",
        "execution_mode": "Client demo - business validation warning",
        "log_path": DEFAULT_LOG_PATH,
        "checks": {
            "Job Status Check": "100%",
            "GD Layer Loading": "100%",
            "DBKR Layer Loading": "100%",
            "CBB Layer Loading": "100%",
            "IVP - Last Modification Check": "Failed",
            "ZOM Workzone Polygon Check": "100%",
        },
        "overall": "85%",
        "logs": [
            "Info: Job status validated successfully",
            "Info: GD layers loaded successfully",
            "Info: DBKR layers loaded successfully",
            "Warning: IVP last modification date mismatch",
            "Error: IVP data is older than expected",
            "Info: ZOM workzone polygon check completed",
            "Info: Process completed with warning",
        ],
    },
    "missing_workzone": {
        "title": "Missing workzone polygon",
        "job_name": "GD-2026-022 / Civil Coordination",
        "execution_mode": "Client demo - geometry validation failure",
        "log_path": DEFAULT_LOG_PATH,
        "checks": {
            "Job Status Check": "100%",
            "GD Layer Loading": "100%",
            "DBKR Layer Loading": "100%",
            "CBB Layer Loading": "100%",
            "IVP - Last Modification Check": "100%",
            "ZOM Workzone Polygon Check": "Failed",
        },
        "overall": "90%",
        "logs": [
            "Info: Job status validated successfully",
            "Info: Layers loaded successfully",
            "Warning: No workzone present for selected extent",
            "Error: ZOM workzone polygon not found",
            "Info: Process completed with errors",
        ],
    },
    "dbkr_slow": {
        "title": "DBKR performance bottleneck",
        "job_name": "GD-2026-031 / Backbone Capacity Upgrade",
        "execution_mode": "Client demo - database performance warning",
        "log_path": DEFAULT_LOG_PATH,
        "checks": {
            "Job Status Check": "100%",
            "GD Layer Loading": "100%",
            "DBKR Layer Loading": "Slow",
            "CBB Layer Loading": "100%",
            "IVP - Last Modification Check": "100%",
            "ZOM Workzone Polygon Check": "100%",
        },
        "overall": "85%",
        "logs": [
            "Info: Job status validated successfully",
            "Warning: DBKR query execution time is high",
            "Info: EXPLAIN ANALYZE completed",
            "Warning: Missing index detected on geometry column",
            "Info: Process completed with performance warning",
        ],
    },
}


def build_log_lines(logs: list[str], timestamp: datetime | None = None) -> list[str]:
    """Add a timestamp prefix so the dashboard looks like an execution trace."""
    now = timestamp or datetime.now()
    formatted_timestamp = now.strftime("%H:%M:%S %d/%m/%Y")
    return [f"-{formatted_timestamp} - {entry}" for entry in logs]


def get_scenario_payload(name: str) -> dict:
    """Return one named scenario in a structure the dialog can render directly."""
    scenario = SCENARIOS[name]
    return {
        "scenario_name": name,
        "title": scenario["title"],
        "job_name": scenario["job_name"],
        "execution_mode": scenario["execution_mode"],
        "log_path": scenario["log_path"],
        "checks": scenario["checks"],
        "overall": scenario["overall"],
        "logs": build_log_lines(scenario["logs"]),
    }
