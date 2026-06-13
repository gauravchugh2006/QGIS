"""Entry helper for running the dashboard directly from the QGIS Python console."""

from qgis_dashboard.dialog import QGISProfileReportDialog


def show_dialog():
    """Create and show the dashboard inside an already running QGIS session."""
    dialog = QGISProfileReportDialog()
    dialog.show()
    return dialog
