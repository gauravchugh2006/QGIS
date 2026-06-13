# QGIS GDE DBKR Profiling Toolkit

## Business Perspective

QGIS is a free, open-source GIS tool used to work with maps, spatial data, and geographic analysis.

From a business point of view, that matters because many teams depend on map-driven decisions for planning, operations, reporting, and field execution. When QGIS-based workflows become slow, unstable, or memory-heavy, the impact is not only technical. It can delay analysis, reduce team productivity, and affect project decisions in areas like land management, utilities, transport, environment, and public-sector work.

This toolkit exists to support that business need. It helps measure performance in QGIS-related Python flows, GDE components, DBKR components, and PostgreSQL-backed workloads so teams can identify bottlenecks early and improve reliability with evidence.

## What QGIS Is Used For

QGIS is commonly used to:

- plot locations on a map
- create thematic maps such as population, rainfall, or land-use maps
- add roads, rivers, boundaries, and satellite imagery
- style maps with labels, symbols, colors, and legends
- export professional maps for reports and presentations

Common business examples:

- property or land maps
- utility network maps
- environmental maps
- delivery route maps
- election maps

## Simple Acronym and Layer Guide

In this project, QGIS acts like a digital map viewer. A simple way to think about it is like a sandwich: each layer is one ingredient stacked on top of another to build the full picture.

### DBKR Layer

- What it means:
  `DataBase King / Kabel Registratie`
- Simple meaning:
  This is the infrastructure layer.
- Why it is used:
  It draws the actual network assets such as underground fiber cables, copper wires, and utility poles.
- Why it matters:
  If this layer fails, the map may be missing the real network that the team needs to inspect, maintain, or build.

### CBB Layer

- What it means:
  `Centrale Background Kaart`
- Simple meaning:
  This is the basemap or background layer.
- Why it is used:
  It provides location context like streets, buildings, and surrounding geography.
- Why it matters:
  Without it, DBKR assets would look like floating lines on a blank screen with no real-world reference.

### IVP Check

- What it means:
  `Informatie Voorzienings Plan`
- Simple meaning:
  This is a data freshness and integrity check.
- Why it is used:
  It checks when the source data was last updated.
- Why it matters:
  If IVP fails, users may be looking at outdated information and could make the wrong field or planning decision.

### ZOM Polygon / Workzone Polygon

- What it means:
  `Zone Op Maat` / Workzone Polygon
- Simple meaning:
  This is the project boundary marker.
- Why it is used:
  A polygon is just a closed shape on the map that marks the exact allowed work area.
- Why it matters:
  If it is missing, teams may not know where the approved work area begins and ends.

### Slow DB Query

- What it means:
  Slow database request
- Simple meaning:
  This is a speed check.
- Why it is used:
  QGIS requests data from a central database. This check highlights when the database response is too slow.
- Why it matters:
  Slow loading wastes time, delays work, and reduces productivity.

### GD / GDE

- What it means:
  `Geospatial Data / Geospatial Desktop Environment`
- Simple meaning:
  This is the company’s custom GIS workspace.
- Why it is used:
  QGIS is the public software platform, while GD/GDE represents the company-specific setup, business layers, and operational tooling built around it.
- Why it matters:
  It is the business-specific environment where jobs, designs, planning layers, and validation checks come together.

## Quick Reference Summary

| Layer / Check | What it actually is | Why it matters to the business |
|---|---|---|
| `CBB` | The background street map | Gives location context |
| `DBKR` | The cables and hardware | Shows the actual network assets |
| `ZOM / Workzone` | A highlighted area boundary | Tells you exactly where to work |
| `IVP Check` | A timestamp validator | Ensures you are not using old or incorrect data |
| `Slow DB Query` | A speed test | Prevents lag and wasted time |

## What QGIS Profiling Means

In QGIS, profiling often means analyzing elevation or terrain along a line or path.

For example:

1. Load terrain or elevation data.
2. Draw a line across a road, hill, corridor, or route.
3. Generate an elevation profile.
4. Study steep slopes, valleys, or visibility constraints.

The result is usually a graph where:

- the X-axis shows distance
- the Y-axis shows elevation

This is useful in:

- road and railway planning
- drainage analysis
- mining and geology
- telecom tower line-of-sight analysis
- hiking trail analysis

## Main QGIS Data Types

- `Vector data`
  Points, lines, and polygons such as buildings, roads, or parcels.
- `Raster data`
  Satellite images, scanned maps, and gridded surfaces.
- `DEM (Digital Elevation Model)`
  Elevation data used for terrain profiling and height analysis.

## Popular QGIS Features

- georeferencing
- spatial analysis
- GPS data handling
- 3D terrain visualization
- heat maps
- buffer and overlay analysis
- plugin support

## Who Uses QGIS

- surveyors
- urban planners
- environmental scientists
- civil engineers
- GIS analysts
- government agencies
- researchers

Official site: [QGIS](https://qgis.org)

## What This Project Is

This project is a profiling toolkit for checking how long important application tasks take, how much CPU they use, and whether memory keeps growing during repeated runs.

It supports internship work around:

- GDE frontend and backend Python flows
- QGIS-native Python-accessible tasks
- DBKR frontend and backend processing
- PostgreSQL query profiling
- Tool research, security review, and reporting

## Why This Project Exists

When a system feels slow or heavy, teams often know the symptom but not the exact reason.

This project helps answer:

- Which task is taking more time?
- Which code path is CPU-heavy?
- Is memory increasing every time the same task runs?
- Is a database query slow by itself?
- Which profiling tools are safe and suitable for company use?

This toolkit gives a repeatable way to collect evidence before suggesting optimization work.

## Problem This Project Solves

Without profiling, developers usually guess:

- "Maybe the frontend is slow."
- "Maybe PostgreSQL is the issue."
- "Maybe there is a memory leak."

This project replaces guessing with measured output files in the `reports/` folder so developers can review facts instead of assumptions.

## Who Should Read This README

This README is written for a junior developer who:

- is new to the project
- wants to understand the need first
- wants to know the folder structure
- wants to know what each module is doing
- wants to run the project locally in Visual Studio Code with fewer setup issues

## High-Level Flow

1. `src/main.py` starts the profiling run.
2. It loads settings from `config/settings.yaml`.
3. It calls the sample GDE, QGIS, and DBKR profiling functions.
4. CPU reports are written into `reports/`.
5. Memory growth is checked over repeated runs.
6. If PostgreSQL is available, query profiling is attempted.
7. A final summary file is created for quick review.

## Data Flow in Simple Language

Each profiling method follows nearly the same pattern:

1. Start with a sample task or a real task later.
2. Measure memory before running it.
3. Run the task.
4. Measure elapsed time or CPU time.
5. Save the result into a report file.
6. Repeat if needed to observe memory growth.

The data flow is:

`config -> workload -> profiler -> report writer -> reports folder`

## Folder Structure and Why It Exists

```text
qgis-gde-dbkr-profiler/
├── README.md
├── requirements.txt
├── .gitignore
├── .env.example
├── config/
├── docs/
├── src/
├── reports/
├── tests/
└── scripts/
```

### `config/`

- `settings.yaml`
  Central place for environment, profiling, and database settings.
- `tool_selection.yaml`
  Approved profiling tools and their licensing/security notes.

### `docs/`

Stores non-code internship deliverables.

- Scope, research, comparison, license review, provisioning notes, HR checklist, and final report all live here.
- This matters because the assignment is not only coding.

### `src/`

Contains the application code.

#### `src/common/`

- `config_loader.py`
  Loads YAML config so other files do not hardcode parsing logic.
- `logger.py`
  Creates a consistent console logger.
- `report_writer.py`
  Writes text and JSON reports to disk.

#### `src/profiling/`

- `elapsed_time_profiler.py`
  Measures wall-clock time. Useful for "how long did this take for the user?"
- `cpu_profiler.py`
  Uses `cProfile` to show which functions consumed runtime.
- `memory_profiler.py`
  Reads current Python process memory usage.
- `memory_leak_checker.py`
  Repeats a function and checks whether memory keeps growing.
- `summary_analyzer.py`
  Converts raw measurements into a short summary.

#### `src/gde/`

- `sample_gde_function.py`
  Holds sample workloads that simulate frontend/backend work.
- `profile_gde_frontend.py`
  Profiles frontend-style processing.
- `profile_gde_backend.py`
  Profiles backend-style processing.

#### `src/qgis_native/`

- `sample_qgis_native_task.py`
  Mock QGIS-like task for now.
- `profile_qgis_native_functions.py`
  Wraps that task with timing and memory checks.

#### `src/qgis_dashboard/`

- `sample_scenarios.py`
  Client-demo scenarios for success, validation failure, missing polygon, and slow DBKR cases.
- `dialog.py`
  Professional PyQt dashboard dialog for QGIS 3 demos.
- `run_from_qgis_console.py`
  Helper for launching the dashboard inside QGIS.
- `run_standalone_demo.py`
  Optional standalone launcher when PyQt is available outside QGIS.

#### `src/dbkr/`

- `profile_dbkr_frontend.py`
  Profiles DBKR frontend-style task flow.
- `profile_dbkr_backend.py`
  Profiles DBKR backend-style processing.
- `postgres_query_profiler.py`
  Runs `EXPLAIN ANALYZE` on PostgreSQL queries.

#### `src/reports/`

- `final_report_builder.py`
  Builds a readable final summary after the run completes.

### `reports/`

This is the output folder.

- `gde/`, `qgis_native/`, `dbkr/`
  CPU reports for each area
- `database/`
  PostgreSQL profiling output
- `memory/`
  Memory growth summary
- `final/`
  Final high-level summary

### `tests/`

Validates the basic reliability of the toolkit.

### `scripts/`

Windows helper scripts for setup and execution.

- `run_qgis_dashboard_demo.bat`
  Starts the standalone dashboard demo if the local machine has PyQt available.

## Method-by-Method Relevance

### `src/main.py`

- `run_database_profile_if_available()`
  Tries PostgreSQL profiling only if enabled and skips cleanly if unavailable.
- `run_all_profiles()`
  Main orchestrator. Loads settings, runs profilers, saves summaries, and builds the final report.

### `src/common/config_loader.py`

- `load_yaml_file()`
  Reads any YAML config file and returns Python data.
- `load_settings()`
  Loads runtime settings.
- `load_tool_selection()`
  Loads the approved tool list.

### `src/common/logger.py`

- `get_logger()`
  Creates a standard logger so console messages stay consistent.

### `src/common/report_writer.py`

- `ensure_parent_dir()`
  Makes sure the target report folder exists.
- `write_text_report()`
  Saves plain text output.
- `write_json_report()`
  Saves structured summaries.

### `src/profiling/elapsed_time_profiler.py`

- `elapsed_time_profile()`
  Decorator that measures total execution time of a function.

### `src/profiling/cpu_profiler.py`

- `run_cpu_profile()`
  Runs a function under `cProfile` and writes a ranked CPU report.

### `src/profiling/memory_profiler.py`

- `get_memory_usage_mb()`
  Returns current process memory in MB.
- `print_memory_usage()`
  Prints memory with a friendly label.

### `src/profiling/memory_leak_checker.py`

- `check_memory_growth()`
  Repeats a function and checks whether memory appears to keep increasing.

### `src/profiling/summary_analyzer.py`

- `build_summary()`
  Turns a list of measurements into a summary for reports.

### `src/gde/sample_gde_function.py`

- `sample_gde_frontend_workload()`
  Simulates frontend data preparation work.
- `sample_gde_backend_workload()`
  Simulates backend computation work.

### `src/gde/profile_gde_frontend.py`

- `profile_gde_frontend_task()`
  Measures memory before and after the GDE frontend sample task.

### `src/gde/profile_gde_backend.py`

- `profile_gde_backend_task()`
  Measures memory before and after the GDE backend sample task.

### `src/qgis_native/sample_qgis_native_task.py`

- `sample_qgis_native_task()`
  Mock task standing in for a real QGIS-native operation.

### `src/qgis_native/profile_qgis_native_functions.py`

- `profile_qgis_native_function()`
  Profiles a QGIS-style function with elapsed time and memory logs.

### `src/dbkr/profile_dbkr_frontend.py`

- `profile_dbkr_frontend_task()`
  Simulates DBKR frontend processing and measures memory around it.

### `src/dbkr/profile_dbkr_backend.py`

- `profile_dbkr_backend_task()`
  Simulates DBKR backend processing and measures memory around it.

### `src/dbkr/postgres_query_profiler.py`

- `profile_postgres_query()`
  Connects to PostgreSQL and runs `EXPLAIN ANALYZE`.

### `src/reports/final_report_builder.py`

- `build_final_report()`
  Combines final messages into one summary file.

## Current Technical Scope

Right now this project is a working baseline toolkit with sample workloads.

That means:

- the profiling engine works
- reports are generated
- tests run
- PostgreSQL profiling works when a database is available
- real production GDE/QGIS/DBKR functions still need to replace the sample methods

## Local Machine Prerequisites

### Required

- Windows 10 or Windows 11
- Visual Studio Code
- Python 3.12.x
- `pip`
- PostgreSQL 15 or PostgreSQL 16

### Recommended

- Git
- PowerShell 7 if available
- VS Code Python extension
- VS Code YAML extension
- VS Code PostgreSQL extension
- PyQt5 for the standalone dashboard demo

### Optional but Useful

- QGIS LTR if you later replace mock QGIS tasks with real QGIS API calls
- pgAdmin for checking PostgreSQL connectivity and test SQL

### Not Required for the Current Baseline

- JDK
- Android SDK
- .NET SDK

Those are not used by the current Python-based toolkit. If your organization has additional wrappers outside this repository, document them separately instead of assuming they are required here.

## Docker Support

This project now includes container support for both:

- local end-to-end runs with PostgreSQL included
- production-style runs where PostgreSQL is external

Added files:

- `Dockerfile`
- `docker-compose.local.yml`
- `docker-compose.production.yml`
- `.env.local.example`
- `.env.production.example`
- `docker/postgres/init/01-init-db.sql`

## Environment Variable Strategy

The code still reads `config/settings.yaml`, but environment variables now override YAML values automatically.

This is useful because:

- local machine runs can use PowerShell or `.env.local`
- Docker runs can use compose env files
- deployed servers can inject secrets and hostnames without editing source code

Important environment variables:

| Variable | Purpose |
|---|---|
| `APP_ENV` | Marks the runtime as `local` or `production` |
| `OUTPUT_DIR` | Controls where generated reports are written |
| `ENABLE_CPU_PROFILE` | Enables or disables CPU profiling |
| `ENABLE_ELAPSED_TIME` | Enables or disables elapsed-time logging |
| `ENABLE_MEMORY_CHECK` | Enables or disables memory checks |
| `ENABLE_DATABASE_PROFILE` | Enables or disables PostgreSQL profiling |
| `TOP_N_FUNCTIONS` | Controls how many cProfile rows to write |
| `MEMORY_LEAK_ITERATIONS` | Controls how many repeated memory test runs happen |
| `DB_HOST` | PostgreSQL hostname |
| `DB_PORT` | PostgreSQL port |
| `DB_NAME` | PostgreSQL database name |
| `DB_USER` | PostgreSQL username |
| `DB_PASSWORD` | PostgreSQL password |
| `DB_TEST_QUERY` | Query used by the PostgreSQL profiler |

## QGIS Dashboard Demo

This project now also includes a client-facing QGIS 3 PyQt dashboard prototype under `src/qgis_dashboard/`.

The dashboard shows:

- job status checks
- GD layer loading checks
- DBKR layer loading checks
- CBB layer loading checks
- IVP last modification checks
- ZOM workzone polygon checks
- overall readiness status
- timestamped execution logs

This dashboard is isolated from the existing CLI profiling workflow, so `src/main.py` and the current reports pipeline continue working as before.

### Run Inside QGIS Python Console

Add the project `src` folder to `sys.path` and launch the helper:

```python
import sys
sys.path.append(r"C:\path\to\qgis-gde-dbkr-profiler\src")

from qgis_dashboard.run_from_qgis_console import show_dialog

dialog = show_dialog()
```

### Run as a Standalone Demo

Install the optional standalone dashboard runtime first:

```powershell
pip install -r requirements-dashboard.txt
```

Then run:

```powershell
python -c "import sys; sys.path.insert(0, 'src'); from qgis_dashboard.run_standalone_demo import main; main()"
```

Or use:

```powershell
scripts\run_qgis_dashboard_demo.bat
```

There is also an install helper:

```powershell
scripts\install_dashboard_runtime.bat
```

### Demo Scenarios

- `success`
  Shows a fully healthy workflow
- `ivp_failed`
  Shows a business validation failure for stale IVP data
- `missing_workzone`
  Shows a missing ZOM polygon issue
- `dbkr_slow`
  Shows a database performance bottleneck

Detailed dashboard setup notes are available in `docs/10_qgis_dashboard_setup.md`.

## PostgreSQL Local Setup Guidance

To run end to end with database profiling enabled, a local PostgreSQL server is needed.

Recommended versions:

- PostgreSQL 15
- PostgreSQL 16

Minimum expectations:

- server installed and running
- port `5432` available locally
- a database named `dbkr` or a custom name you place in `config/settings.yaml`
- a user that can connect from localhost

Current expected config:

```yaml
database:
  host: localhost
  port: 5432
  database: dbkr
  user: postgres
  password: postgres
  test_query: SELECT 1
```

If you use Docker local compose, PostgreSQL is provided automatically and seeded with a small sample table.

## Visual Studio Code Setup

1. Open Visual Studio Code.
2. Open the folder `qgis-gde-dbkr-profiler`.
3. Open the integrated terminal.
4. Confirm Python is installed:

```powershell
python --version
```

5. Create the virtual environment:

```powershell
python -m venv .venv
```

6. Activate it:

```powershell
.\.venv\Scripts\activate
```

7. Install dependencies:

```powershell
pip install -r requirements.txt
```

8. If VS Code asks for a Python interpreter, select `.venv`.

## Local Machine Run Without Docker

1. Copy `.env.local.example` to `.env.local` if you want an easy reference file.
2. Export the values in your PowerShell session if you want them to override YAML.
3. Or keep using `config/settings.yaml` directly.

Example PowerShell override:

```powershell
$env:APP_ENV="local"
$env:DB_HOST="localhost"
$env:DB_PORT="5432"
$env:DB_NAME="dbkr"
$env:DB_USER="postgres"
$env:DB_PASSWORD="postgres"
python src/main.py
```

## Docker Local Run

This mode is for a developer who wants the toolkit and PostgreSQL together.

1. Copy the local env template:

```powershell
Copy-Item .env.local.example .env.local
```

2. Start the local stack:

```powershell
docker compose -f docker-compose.local.yml up --build
```

3. Stop it when done:

```powershell
docker compose -f docker-compose.local.yml down
```

What this local stack does:

- builds the Python app container
- starts PostgreSQL 16
- creates the `dbkr` database
- seeds a sample table called `public.sample_assets`
- runs the profiling toolkit after PostgreSQL becomes healthy

Generated reports still appear on your host machine under `reports/`.

## Production-Style Container Run

This mode is for a deployed server where PostgreSQL already exists outside the container stack.

1. Copy the production env template:

```powershell
Copy-Item .env.production.example .env.production
```

2. Replace the placeholder DB host, username, and password with real values.

3. Start the app container:

```powershell
docker compose -f docker-compose.production.yml up --build
```

In this mode:

- no PostgreSQL container is created
- the app connects to the external database from env vars
- this is closer to how a real server deployment should work

## Switching Between Local and Production

Use this rule:

- for local laptop testing with bundled PostgreSQL: `docker-compose.local.yml` and `.env.local`
- for production server or UAT server with external PostgreSQL: `docker-compose.production.yml` and `.env.production`

You do not need to edit Python code when switching. Only the environment variables and compose file change.

## Full Local Run

Run the full profiling toolkit:

```powershell
python src/main.py
```

Run tests:

```powershell
pytest
```

Or use helper scripts:

```powershell
scripts\setup_env.bat
scripts\run_all_profiles.bat
scripts\run_tests.bat
```

If Docker is preferred for local end-to-end validation, use the compose commands shown above instead.

## What Output You Should Expect

After a successful run, you should see generated files under:

- `reports/gde/`
- `reports/qgis_native/`
- `reports/dbkr/`
- `reports/memory/`
- `reports/final/`

If PostgreSQL is reachable, you should also see output under `reports/database/`.

## Common Local Issues

### Python command not found

Cause:
Python is not installed or not added to `PATH`.

Fix:
Reinstall Python and enable the `Add Python to PATH` option.

### Virtual environment not activating

Cause:
PowerShell execution policy may block activation scripts.

Fix:

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

### PostgreSQL connection refused

Cause:
PostgreSQL is not running, wrong port is used, or credentials are incorrect.

Fix:

- check the PostgreSQL service
- confirm host, port, username, and password
- verify the `dbkr` database exists
- test the same credentials in `psql` or pgAdmin

If you want to avoid manual local PostgreSQL setup, use `docker-compose.local.yml`.

### QGIS-specific code does not run later

Cause:
Real QGIS Python API work usually needs QGIS installed and environment variables aligned.

Fix:
Keep the current sample implementation until the real QGIS runtime path is defined by the team.

## Requirement Mapping

| Requirement | Coverage |
|---|---|
| Tool research | `docs/02_state_of_art_tools.md` |
| Tool selection and comparison | `docs/03_tool_comparison_matrix.md` |
| Security and license checks | `docs/04_security_license_checklist.md` |
| Provisioning support | `docs/05_provisioning_intake.md` |
| GDE profiling | `src/gde/` |
| QGIS profiling | `src/qgis_native/` |
| DBKR profiling | `src/dbkr/` |
| Memory leak notes | `src/profiling/memory_leak_checker.py` and `docs/06_memory_leak_corruption_notes.md` |
| Final reporting | `src/reports/final_report_builder.py` and `docs/09_final_internship_report.md` |

## Suggested Next Step for a Junior Developer

1. Read this `README.md`.
2. Open `config/settings.yaml`.
3. Read `src/main.py`.
4. Read `src/profiling/`.
5. Run `pytest`.
6. Run `python src/main.py`.
7. Open the generated `reports/` files.
8. Replace sample workloads with real project functions one by one.
