"""Profile a GDE backend-like flow with memory and elapsed-time checks."""

from profiling.elapsed_time_profiler import elapsed_time_profile
from profiling.memory_profiler import print_memory_usage

from gde.sample_gde_function import sample_gde_backend_workload


@elapsed_time_profile
def profile_gde_backend_task():
    """Run the sample GDE backend workload and log memory around it."""
    print_memory_usage("GDE backend before")
    result = sample_gde_backend_workload()
    print_memory_usage("GDE backend after")
    return result
