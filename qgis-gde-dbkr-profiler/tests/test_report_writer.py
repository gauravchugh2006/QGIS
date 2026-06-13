"""Verify report writer helpers create folders and save content correctly."""

from common.report_writer import write_json_report, write_text_report


def test_write_text_report_creates_file(tmp_path):
    """Ensure plain text reports are written to nested folders when needed."""
    target = tmp_path / "nested" / "report.txt"
    write_text_report(target, "hello")

    assert target.exists()
    assert target.read_text(encoding="utf-8") == "hello"


def test_write_json_report_creates_file(tmp_path):
    """Ensure JSON reports are written and contain the expected payload."""
    target = tmp_path / "nested" / "report.json"
    write_json_report(target, {"status": "ok"})

    content = target.read_text(encoding="utf-8")
    assert target.exists()
    assert '"status": "ok"' in content
