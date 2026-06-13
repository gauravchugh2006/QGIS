"""Read current process memory so tasks can be compared before and after run."""

import os

import psutil


def get_memory_usage_mb():
    """Return resident memory in MB for the current Python process."""
    process = psutil.Process(os.getpid())
    return process.memory_info().rss / 1024 / 1024


def print_memory_usage(label):
    """Print memory with a label to show where in the flow it was measured."""
    memory_mb = get_memory_usage_mb()
    print(f"[MEMORY] {label}: {memory_mb:.2f} MB")
    return memory_mb
