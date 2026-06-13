"""Run the dashboard outside QGIS when PyQt is available on the local machine."""

from qgis_dashboard.dialog import launch_dashboard


def main():
    """Launch the dashboard event loop for standalone demo or screenshot capture."""
    app, _dialog = launch_dashboard()
    app.exec_()


if __name__ == "__main__":
    main()
