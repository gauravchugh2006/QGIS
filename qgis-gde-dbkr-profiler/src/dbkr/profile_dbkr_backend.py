"""Profile a DBKR backend-like path with sample record generation work."""

from profiling.elapsed_time_profiler import elapsed_time_profile
from profiling.memory_profiler import print_memory_usage


@elapsed_time_profile
def profile_dbkr_backend_task():
    """Simulate DBKR backend object creation and log memory around the task."""
    print_memory_usage("DBKR backend before")

    result = []
    for i in range(60000):
        result.append({"id": i, "value": i * 10})

    print_memory_usage("DBKR backend after")
    return result
