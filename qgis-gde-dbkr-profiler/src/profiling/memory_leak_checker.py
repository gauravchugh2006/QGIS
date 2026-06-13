"""Repeat a task several times to look for suspicious memory growth trends."""

import gc
import time

from profiling.memory_profiler import get_memory_usage_mb


def check_memory_growth(function_to_test, iterations=5, sleep_seconds=0.1):
    """Run the same function repeatedly and record memory after each run."""
    memory_results = []

    for i in range(iterations):
        function_to_test()
        gc.collect()
        time.sleep(sleep_seconds)

        memory_mb = get_memory_usage_mb()
        memory_results.append(memory_mb)

        print(f"[MEMORY LEAK CHECK] Iteration {i + 1}: {memory_mb:.2f} MB")

    growth = memory_results[-1] - memory_results[0]

    if growth > 50:
        print("[WARNING] Possible memory leak detected.")
    else:
        print("[OK] No major memory growth detected.")

    return memory_results
