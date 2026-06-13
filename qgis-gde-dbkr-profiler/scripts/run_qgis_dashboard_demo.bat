REM Launches the standalone QGIS profiling dashboard when PyQt is available locally.
@echo off
call .venv\Scripts\activate
python -c "import importlib.util, sys; sys.exit(0 if importlib.util.find_spec('PyQt5') else 1)"
if errorlevel 1 (
    echo PyQt5 is not installed. Run scripts\install_dashboard_runtime.bat first.
    exit /b 1
)
python -c "import sys; sys.path.insert(0, 'src'); from qgis_dashboard.run_standalone_demo import main; main()"
