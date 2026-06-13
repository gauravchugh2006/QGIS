"""Verify memory helper functions return values and print readable labels."""

from profiling.memory_profiler import get_memory_usage_mb, print_memory_usage


def test_get_memory_usage_mb_returns_number():
    """Check that current memory usage is returned as a positive float."""
    memory_mb = get_memory_usage_mb()
    assert isinstance(memory_mb, float)
    assert memory_mb > 0


def test_print_memory_usage_emits_label(capsys):
    """Check that printed memory output contains the caller-provided label."""
    memory_mb = print_memory_usage("unit-test")
    captured = capsys.readouterr()

    assert isinstance(memory_mb, float)
    assert "[MEMORY] unit-test:" in captured.out
