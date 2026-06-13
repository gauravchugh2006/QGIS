"""Verify CPU profiling writes a report file for a simple sample function."""

from pathlib import Path

from profiling.cpu_profiler import run_cpu_profile


def test_run_cpu_profile_creates_report(tmp_path):
    """Ensure cProfile output is saved and still returns the function result."""
    output_file = tmp_path / "cpu_report.txt"

    def sample():
        return sum(range(100))

    result = run_cpu_profile(sample, output_file, top_n=5)

    assert result == 4950
    assert output_file.exists()
    assert "sample" in output_file.read_text(encoding="utf-8")
