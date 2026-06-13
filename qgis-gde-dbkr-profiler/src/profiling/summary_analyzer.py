"""Convert raw numeric measurements into a short summary for reports."""

from statistics import mean


def build_summary(profile_name: str, measurements: list[float]) -> dict:
    """Summarize sample count, min, max, average, and total growth."""
    if not measurements:
        return {
            "profile_name": profile_name,
            "samples": 0,
            "min": 0,
            "max": 0,
            "average": 0,
            "growth": 0,
        }

    return {
        "profile_name": profile_name,
        "samples": len(measurements),
        "min": min(measurements),
        "max": max(measurements),
        "average": mean(measurements),
        "growth": measurements[-1] - measurements[0],
    }
