"""Verify the elapsed-time decorator preserves results and emits timing logs."""

from profiling.elapsed_time_profiler import elapsed_time_profile


def test_elapsed_time_decorator_returns_result(capsys):
    """Check that the decorator returns the original value and prints timing."""
    @elapsed_time_profile
    def sample():
        return 42

    result = sample()
    captured = capsys.readouterr()

    assert result == 42
    assert "[ELAPSED TIME] sample:" in captured.out
