"""Verify the non-GUI dashboard scenario payloads and timestamped logs."""

from datetime import datetime

from qgis_dashboard.sample_scenarios import CHECK_LABELS, build_log_lines, get_scenario_payload


def test_build_log_lines_adds_timestamp():
    """Ensure the dashboard log helper prepends the expected execution timestamp."""
    lines = build_log_lines(["Info: sample"], timestamp=datetime(2026, 6, 13, 10, 5, 1))

    assert lines == ["-10:05:01 13/06/2026 - Info: sample"]


def test_get_scenario_payload_contains_all_expected_checks():
    """Ensure each scenario payload is ready for the dialog without missing checks."""
    payload = get_scenario_payload("success")

    assert payload["scenario_name"] == "success"
    assert set(payload["checks"].keys()) == set(CHECK_LABELS)
    assert payload["overall"] == "100%"
    assert payload["logs"]
