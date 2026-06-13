"""Profile a DBKR frontend-like path with simple in-memory sample data."""

from profiling.elapsed_time_profiler import elapsed_time_profile
from profiling.memory_profiler import print_memory_usage


@elapsed_time_profile
def profile_dbkr_frontend_task():
    """Simulate DBKR frontend filtering work and log memory around the task."""
    print_memory_usage("DBKR frontend before")
    rows = [f"record-{i}" for i in range(40000)]
    filtered = [row for row in rows if row.endswith(("0", "5"))]
    print_memory_usage("DBKR frontend after")
    return filtered
