"""Profile a GDE frontend-like flow with memory and elapsed-time checks."""

from profiling.elapsed_time_profiler import elapsed_time_profile
from profiling.memory_profiler import print_memory_usage

from gde.sample_gde_function import sample_gde_frontend_workload


@elapsed_time_profile
def profile_gde_frontend_task():
    """Run the sample GDE frontend workload and log memory around it."""
    print_memory_usage("GDE frontend before")
    data = sample_gde_frontend_workload()
    print_memory_usage("GDE frontend after")
    return data
