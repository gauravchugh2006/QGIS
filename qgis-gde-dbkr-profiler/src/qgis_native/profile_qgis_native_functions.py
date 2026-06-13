"""Profile a QGIS-style function without requiring a live QGIS install yet."""

from profiling.elapsed_time_profiler import elapsed_time_profile
from profiling.memory_profiler import print_memory_usage

from qgis_native.sample_qgis_native_task import sample_qgis_native_task


@elapsed_time_profile
def profile_qgis_native_function():
    """Run the sample QGIS task and show elapsed time plus memory markers."""
    print_memory_usage("QGIS native function before")
    processed_layers = sample_qgis_native_task()
    print_memory_usage("QGIS native function after")
    return processed_layers
