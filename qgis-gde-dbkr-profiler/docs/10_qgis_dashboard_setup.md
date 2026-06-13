# QGIS Dashboard Setup

## Purpose

This document explains how to run the client-demo dashboard added under `src/qgis_dashboard/`.

The dashboard can run in two modes:

- `QGIS mode`
  Launch inside QGIS Python Console using QGIS-bundled PyQt.
- `Standalone mode`
  Launch outside QGIS using `PyQt5` installed in the project virtual environment.

## Recommended Prerequisites

### For standalone demo mode

- Windows 10 or Windows 11
- Python 3.12.x
- Project virtual environment created
- `PyQt5` installed

### For QGIS-integrated mode

- QGIS LTR or QGIS 3.x Desktop installed locally
- Access to QGIS Python Console
- Project source folder available on disk

## Install Standalone Dashboard Runtime

```powershell
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
pip install -r requirements-dashboard.txt
```

## Run Standalone Dashboard

```powershell
scripts\run_qgis_dashboard_demo.bat
```

## Run Inside QGIS

Open QGIS, then open the Python Console and run:

```python
import sys
sys.path.append(r"C:\path\to\qgis-gde-dbkr-profiler\src")

from qgis_dashboard.run_from_qgis_console import show_dialog

dialog = show_dialog()
```

## How to Verify It Is Working

You should see:

- a dialog titled `QGIS 3 Profiling Dashboard`
- a scenario dropdown
- status bars for job, GD, DBKR, CBB, IVP, and ZOM checks
- an overall status bar
- a bottom log viewer with timestamps

Switch between scenarios:

- `success`
- `ivp_failed`
- `missing_workzone`
- `dbkr_slow`

Verify that:

- progress bar colors change correctly
- the overall status changes
- the bottom log text updates
- the dialog closes cleanly
