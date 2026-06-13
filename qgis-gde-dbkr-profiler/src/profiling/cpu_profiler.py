"""Capture CPU hotspots using cProfile and save the ranked output to disk."""

import cProfile
import io
import pstats
from pathlib import Path

from common.report_writer import write_text_report


def run_cpu_profile(function_to_profile, output_file: str | Path, top_n: int = 30):
    """Run one function under cProfile and write the top expensive calls."""
    profiler = cProfile.Profile()
    profiler.enable()

    result = function_to_profile()

    profiler.disable()

    stream = io.StringIO()
    stats = pstats.Stats(profiler, stream=stream)
    stats.sort_stats("cumulative")
    stats.print_stats(top_n)
    write_text_report(output_file, stream.getvalue())

    print(f"[CPU PROFILE] Saved: {output_file}")
    return result
