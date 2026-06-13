## What is QGIS?

**QGIS** is a desktop GIS application. GIS means **Geographic Information System**.

In simple words, QGIS is used to view, edit, analyze, and manage map-based data.

Example map data:

* roads
* buildings
* parcels
* cables
* poles
* work zones
* underground network assets
* customer/service areas

So instead of seeing only rows in a database, QGIS shows that data visually on a map.

---

## What are layers in QGIS?

A **layer** is one category of map data.

Example:

| Layer             | Meaning                                       |
| ----------------- | --------------------------------------------- |
| Roads layer       | Shows roads                                   |
| Buildings layer   | Shows building polygons                       |
| Parcels layer     | Shows land boundaries                         |
| DBKR layer        | Shows database-backed enterprise network data |
| CBB layer         | Shows background cartography                  |
| ZOM polygon layer | Shows selected workzone area                  |

Each layer can come from a file, database, API, or enterprise GIS system.

---

## What is GD / GDE in this context?

In your project context, **GD/GDE** looks like an enterprise-specific geospatial application/data module used inside QGIS.

You can explain it like this:

**GD/GDE layers are business-specific geospatial layers loaded into QGIS to represent operational network or project data.**

They may include:

* design data
* workzone boundaries
* project geometry
* network infrastructure
* planning layers
* backend GIS/database-loaded data

So, GD/GDE is not a standard QGIS term like “vector layer” or “raster layer”. It is likely a company/project-specific naming convention.

---

## Why are these terms used in reports?

Because the report is not only about coding. It is about proving that the QGIS/GDE solution works correctly in a business workflow.

The report must answer:

```text
Can the user open the job?
Are required layers loaded?
Is database data available?
Is the map complete?
Is the workzone valid?
Is the data fresh?
Is loading slow?
Where did the failure happen?
```

That is why the report contains checks like:

```text
Job Status Check
GD Layer Loading
DBKR Layer Loading
CBB Layer Loading
IVP Last Modification Check
ZOM Workzone Polygon Check
```

---

## Business objective

The business objective is to make sure the GIS user can safely and efficiently work on a network/project map.

For example, a telecom company may use QGIS/GDE to plan or validate:

* fibre/copper network design
* underground infrastructure
* work zones
* excavation planning
* project boundaries
* customer/service coverage
* field execution plans

If one layer fails, the business impact can be serious.

Example:

| Failure             | Business impact                       |
| ------------------- | ------------------------------------- |
| DBKR layer fails    | Network data may not load             |
| CBB layer fails     | User loses map background/context     |
| IVP check fails     | User may work on outdated data        |
| ZOM polygon missing | Wrong workzone may be processed       |
| Slow DB query       | User loses time, poor productivity    |
| Job status invalid  | Wrong or incomplete job may be opened |

---

## Why enterprises implement these checks

Enterprises use these measures to reduce manual mistakes.

Without such checks, a user may open QGIS and assume everything is fine, but actually:

* one database layer did not load
* some geometry is missing
* data is outdated
* a query is too slow
* workzone polygon is absent
* logs are hidden or hard to read

The dashboard makes this visible immediately.

---

## Simple explanation for your TFE report

You can write:

> QGIS is used as the geospatial desktop environment where business and technical map layers are loaded, validated, and analyzed. GD/GDE layers represent enterprise-specific geospatial data required for the operational workflow. The profiling dashboard validates whether each required layer and business check has completed successfully. This helps identify missing data, slow database loading, outdated information, and invalid workzones before the user starts working on the map. The objective is to improve reliability, reduce manual investigation, and support faster troubleshooting of QGIS-based business operations.
------
Yes, Now after understanding QGIS and its related terms and acronyms,  lets build it as a **QGIS 3 PyQt dialog/profiling dashboard**. It will show:

Job checks, layer loading checks, DBKR/CBB loading, modification checks, ZOM polygon checks, overall status, and a bottom log section with execution date/time.

Use this as your TFE demo scenario.

```text
qgis3_profile_report/
│
├── qgis_profile_dialog.py
├── sample_scenarios.py
└── run_from_qgis_console.py
```

### 1. `sample_scenarios.py`

```python
from datetime import datetime

SCENARIOS = {
    "success": {
        "Job Status Check": "100%",
        "GD Layer Loading": "100%",
        "DBKR Layer Loading": "100%",
        "CBB Layer Loading": "100%",
        "IVP - Last Modification Check": "100%",
        "ZOM Workzone Polygon Check": "100%",
        "overall": "100%",
        "logs": [
            "Info: Job status validated successfully",
            "Info: GD layers loaded successfully",
            "Info: DBKR PostgreSQL layers loaded successfully",
            "Info: CBB background layers loaded successfully",
            "Info: IVP last modification date verified",
            "Info: ZOM workzone polygon found",
            "Info: Process Completed"
        ]
    },

    "ivp_failed": {
        "Job Status Check": "100%",
        "GD Layer Loading": "100%",
        "DBKR Layer Loading": "100%",
        "CBB Layer Loading": "100%",
        "IVP - Last Modification Check": "Failed",
        "ZOM Workzone Polygon Check": "100%",
        "overall": "100%",
        "logs": [
            "Info: Job status validated successfully",
            "Info: GD layers loaded successfully",
            "Info: DBKR layers loaded successfully",
            "Warning: IVP last modification date mismatch",
            "Error: IVP data is older than expected",
            "Info: ZOM Workzone Polygon Check completed",
            "Info: Process Completed with warning"
        ]
    },

    "missing_workzone": {
        "Job Status Check": "100%",
        "GD Layer Loading": "100%",
        "DBKR Layer Loading": "100%",
        "CBB Layer Loading": "100%",
        "IVP - Last Modification Check": "100%",
        "ZOM Workzone Polygon Check": "Failed",
        "overall": "90%",
        "logs": [
            "Info: Job status validated successfully",
            "Info: Layers loaded successfully",
            "Warning: No Workzone Present for selected extent",
            "Error: ZOM Workzone Polygon not found",
            "Info: Process Completed with errors"
        ]
    },

    "dbkr_slow": {
        "Job Status Check": "100%",
        "GD Layer Loading": "100%",
        "DBKR Layer Loading": "Slow",
        "CBB Layer Loading": "100%",
        "IVP - Last Modification Check": "100%",
        "ZOM Workzone Polygon Check": "100%",
        "overall": "85%",
        "logs": [
            "Info: Job status validated successfully",
            "Warning: DBKR query execution time is high",
            "Info: EXPLAIN ANALYZE completed",
            "Warning: Missing index detected on geometry column",
            "Info: Process Completed with performance warning"
        ]
    }
}


def build_log_lines(logs):
    now = datetime.now()
    lines = []
    for log in logs:
        timestamp = now.strftime("%H:%M:%S %d/%m/%Y")
        lines.append(f"-{timestamp} - {log}")
    return lines
```

### 2. `qgis_profile_dialog.py`

```python
from qgis.PyQt.QtWidgets import (
    QDialog, QVBoxLayout, QGridLayout, QLabel,
    QProgressBar, QTextEdit, QPushButton, QComboBox
)
from qgis.PyQt.QtCore import Qt
from sample_scenarios import SCENARIOS, build_log_lines


class QGISProfileReportDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QGIS3 - Open GD")
        self.resize(620, 560)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        title = QLabel("Open GD")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("font-weight: bold; font-size: 16px;")
        self.layout.addWidget(title)

        self.scenario_box = QComboBox()
        self.scenario_box.addItems(SCENARIOS.keys())
        self.scenario_box.currentTextChanged.connect(self.load_scenario)
        self.layout.addWidget(self.scenario_box)

        self.grid = QGridLayout()
        self.layout.addLayout(self.grid)

        self.rows = {}
        labels = [
            "Job Status Check",
            "GD Layer Loading",
            "DBKR Layer Loading",
            "CBB Layer Loading",
            "IVP - Last Modification Check",
            "ZOM Workzone Polygon Check"
        ]

        for i, label in enumerate(labels):
            text = QLabel(label + ":")
            progress = QProgressBar()
            progress.setAlignment(Qt.AlignCenter)
            self.grid.addWidget(text, i, 0)
            self.grid.addWidget(progress, i, 1)
            self.rows[label] = progress

        self.overall_label = QLabel("Overall Status:")
        self.overall_bar = QProgressBar()
        self.overall_bar.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.overall_label)
        self.layout.addWidget(self.overall_bar)

        self.log_path = QLabel(r"C:\Users\Public\Documents\GDE\LOG\Log_20260514150607.txt")
        self.layout.addWidget(self.log_path)

        self.logs = QTextEdit()
        self.logs.setReadOnly(True)
        self.layout.addWidget(self.logs)

        close_btn = QPushButton("Close")
        close_btn.clicked.connect(self.close)
        self.layout.addWidget(close_btn)

        self.load_scenario("success")

    def set_bar(self, bar, value):
        if value == "Failed":
            bar.setValue(100)
            bar.setFormat("Failed")
            bar.setStyleSheet("QProgressBar::chunk { background-color: red; }")
        elif value == "Slow":
            bar.setValue(70)
            bar.setFormat("Slow")
            bar.setStyleSheet("QProgressBar::chunk { background-color: orange; }")
        else:
            percent = int(value.replace("%", ""))
            bar.setValue(percent)
            bar.setFormat(value)
            bar.setStyleSheet("QProgressBar::chunk { background-color: green; }")

    def load_scenario(self, scenario_name):
        data = SCENARIOS[scenario_name]

        for key, bar in self.rows.items():
            self.set_bar(bar, data[key])

        self.set_bar(self.overall_bar, data["overall"])

        log_lines = build_log_lines(data["logs"])
        self.logs.setPlainText("\n".join(log_lines))
```

### 3. Run from QGIS Python Console

```python
import sys
sys.path.append(r"C:\path\to\qgis3_profile_report")

from qgis_profile_dialog import QGISProfileReportDialog

dialog = QGISProfileReportDialog()
dialog.show()
```

### Scenarios to show in your report

Use these screenshots in your TFE report:

| Scenario           | What it proves                                   |
| ------------------ | ------------------------------------------------ |
| `success`          | All QGIS/GDE/DBKR/CBB checks completed correctly |
| `ivp_failed`       | Tool can detect business validation failure      |
| `missing_workzone` | Tool can detect missing ZOM polygon              |
| `dbkr_slow`        | Tool can detect PostgreSQL performance issue     |

### Measures you can explain

| Measure                     | Meaning                                                |
| --------------------------- | ------------------------------------------------------ |
| Job Status Check            | Validates whether the selected job/work order is ready |
| GD Layer Loading            | Checks whether GDE/GD layers are loaded                |
| DBKR Layer Loading          | Checks DBKR PostgreSQL spatial data loading            |
| CBB Layer Loading           | Checks background cartographic layer loading           |
| IVP Last Modification Check | Confirms data freshness                                |
| ZOM Workzone Polygon Check  | Confirms selected workzone polygon exists              |
| Logs                        | Shows execution trace with timestamp                   |
| Overall Status              | Final technical/business readiness result              |

For TFE, present this as a **prototype profiling and validation dashboard for QGIS 3**, used to identify loading failures, slow DBKR queries, stale IVP data, missing polygons, and execution flow issues.

------
Below is the proper explanation you can write in your TFE report.

## 1. Main idea of the code

The QGIS 3 profiling window is a small **PyQt dialog inside QGIS**.
Its job is to show whether the main business and technical steps completed correctly:

```text
Job check → GD layers → DBKR layers → CBB layers → IVP freshness → ZOM polygon → overall result
```

Each row represents one validation point.
The bottom log section records what happened with date and time.

---

## 2. `SCENARIOS` dictionary

```python
SCENARIOS = {
    "success": {
        "Job Status Check": "100%",
        ...
    }
}
```

This is sample test data.

It helps you demonstrate multiple real-life situations without depending on the real production database.

Why used:

It allows testing:

* complete success
* IVP validation failure
* missing workzone polygon
* slow DBKR query

In a real project, these values will come from QGIS layers, PostgreSQL queries, file checks, and business rules.

---

## 3. `build_log_lines()`

```python
def build_log_lines(logs):
    now = datetime.now()
    lines = []
    for log in logs:
        timestamp = now.strftime("%H:%M:%S %d/%m/%Y")
        lines.append(f"-{timestamp} - {log}")
    return lines
```

This function adds execution time and date to every log line.

Example output:

```text
-15:07:35 14/05/2026 - Info: GD layers loaded successfully
```

Why used:

It proves when each validation happened.
This is important for debugging, audit, and performance investigation.

---

## 4. `QGISProfileReportDialog`

```python
class QGISProfileReportDialog(QDialog):
```

This creates the popup window inside QGIS 3.

It uses PyQt because QGIS desktop UI itself is based on Qt/PyQt.

Why used:

It allows the profiling result to appear directly inside QGIS instead of only in terminal output.

---

## 5. Window setup

```python
self.setWindowTitle("QGIS3 - Open GD")
self.resize(620, 560)
```

This sets the title and window size.

Why used:

It makes the tool look like a real QGIS business plugin window.

---

## 6. Scenario dropdown

```python
self.scenario_box = QComboBox()
self.scenario_box.addItems(SCENARIOS.keys())
self.scenario_box.currentTextChanged.connect(self.load_scenario)
```

This dropdown lets you switch between demo cases.

Why used:

For your report and presentation, you can easily show different inputs and different results.

Example:

```text
success
ivp_failed
missing_workzone
dbkr_slow
```

---

## 7. Layer/check rows

```python
labels = [
    "Job Status Check",
    "GD Layer Loading",
    "DBKR Layer Loading",
    "CBB Layer Loading",
    "IVP - Last Modification Check",
    "ZOM Workzone Polygon Check"
]
```

These are the actual checks shown in the UI.

### Job Status Check

Validates whether the selected job is ready to open.

Why used:

Before loading maps and layers, the system must confirm the job exists and is usable.

Possible logic:

```python
job_id is not None
job_status in ["READY", "OPEN", "VALIDATED"]
```

### GD Layer Loading

Checks whether GD/GDE layers loaded correctly in QGIS.

Why used:

These are the main project layers. If they fail, the user cannot work with the GD data.

Possible logic:

```python
QgsProject.instance().mapLayersByName("GD_LAYER")
```

### DBKR Layer Loading

Checks whether DBKR PostgreSQL layers loaded.

Why used:

DBKR is database-backed. This check helps detect database connection or query problems.

Possible logic:

```python
layer.isValid()
provider.name() == "postgres"
```

### CBB Layer Loading

Checks whether background cartographic layers loaded.

Why used:

CBB gives map context such as roads, buildings, parcels, boundaries.

Possible logic:

```python
layer.isValid()
layer.featureCount() > 0
```

### IVP Last Modification Check

Checks whether IVP data is fresh.

Why used:

A layer can load successfully but still contain outdated business data.

Possible logic:

```python
last_modified_date >= expected_date
```

### ZOM Workzone Polygon Check

Checks whether the selected workzone polygon exists.

Why used:

Without a workzone polygon, the tool cannot correctly restrict profiling to the required area.

Possible logic:

```python
workzone_layer.featureCount() > 0
```

---

## 8. Progress bars

```python
progress = QProgressBar()
progress.setAlignment(Qt.AlignCenter)
```

Each check uses a progress bar.

Why used:

It gives a quick visual status:

```text
Green  = success
Red    = failed
Orange = slow/performance warning
Grey   = completed but neutral/warning
```

This is easier to understand than only text logs.

---

## 9. `set_bar()` function

```python
def set_bar(self, bar, value):
```

This function controls how each result is displayed.

### Failed case

```python
if value == "Failed":
    bar.setValue(100)
    bar.setFormat("Failed")
    bar.setStyleSheet("QProgressBar::chunk { background-color: red; }")
```

Used when validation fails.

Example:

```text
IVP Last Modification Check = Failed
```

Why red:

It shows a business or technical blocker.

### Slow case

```python
elif value == "Slow":
    bar.setValue(70)
    bar.setFormat("Slow")
    bar.setStyleSheet("QProgressBar::chunk { background-color: orange; }")
```

Used when something works but performance is not good.

Example:

```text
DBKR Layer Loading = Slow
```

Why orange:

It is not a full failure, but it needs optimization.

### Success case

```python
else:
    percent = int(value.replace("%", ""))
    bar.setValue(percent)
    bar.setFormat(value)
    bar.setStyleSheet("QProgressBar::chunk { background-color: green; }")
```

Used when the check completes successfully.

Example:

```text
GD Layer Loading = 100%
```

---

## 10. `load_scenario()`

```python
def load_scenario(self, scenario_name):
    data = SCENARIOS[scenario_name]
```

This loads one complete test case into the UI.

It updates:

```text
all check bars
overall status
bottom logs
```

Why used:

It separates test data from UI code.
That makes the tool easier to maintain.

---

## 11. Log window

```python
self.logs = QTextEdit()
self.logs.setReadOnly(True)
```

This creates the log section at the bottom.

Why used:

The user can see the detailed execution trace.

Example:

```text
Info: Job status validated successfully
Warning: DBKR query execution time is high
Error: IVP data is older than expected
```

This helps explain what happened behind the progress bars.

---

## 12. Overall Status

```python
self.overall_bar = QProgressBar()
```

This gives the final status of the complete process.

Why used:

Business users do not want to inspect every log line.
They need one final result:

```text
100% = ready
90% = minor issue
85% = performance warning
Failed = blocker
```

---

## 13. How this solves the business problem

This UI helps the QGIS/GDE team quickly answer:

```text
Did the job load correctly?
Did all required layers load?
Is DBKR slow?
Is CBB available?
Is IVP data fresh?
Is the workzone polygon present?
Where did the process fail?
When did it fail?
```

So instead of manually checking logs, layers, and database behavior, the user gets one clear profiling dashboard.

---

## 14. How to explain it in your report

You can write:

> The proposed QGIS 3 profiling dashboard provides a visual validation layer over the GDE loading process. It checks the availability and performance of job status, GD layers, DBKR PostgreSQL layers, CBB background layers, IVP modification freshness, and ZOM workzone polygon availability. Each check is represented by a progress indicator and detailed logs with execution timestamp. This helps identify technical failures, slow database loading, stale data, and missing polygon issues before the user starts working on the map.
