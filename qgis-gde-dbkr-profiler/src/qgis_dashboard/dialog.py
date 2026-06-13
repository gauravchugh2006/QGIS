"""Render a QGIS-style profiling dashboard dialog for client-facing demos."""

try:
    from qgis.PyQt.QtCore import Qt
    from qgis.PyQt.QtWidgets import (
        QApplication,
        QComboBox,
        QDialog,
        QFrame,
        QGridLayout,
        QHBoxLayout,
        QLabel,
        QProgressBar,
        QPushButton,
        QTextEdit,
        QVBoxLayout,
        QWidget,
    )
except ImportError:  # pragma: no cover - exercised only in QGIS/PyQt runtime
    from PyQt5.QtCore import Qt
    from PyQt5.QtWidgets import (
        QApplication,
        QComboBox,
        QDialog,
        QFrame,
        QGridLayout,
        QHBoxLayout,
        QLabel,
        QProgressBar,
        QPushButton,
        QTextEdit,
        QVBoxLayout,
        QWidget,
    )

from qgis_dashboard.sample_scenarios import CHECK_LABELS, SCENARIOS, get_scenario_payload


class QGISProfileReportDialog(QDialog):
    """Show business and technical QGIS validation checks in one professional dialog."""

    def __init__(self):
        """Build the full dashboard UI and load the default client-demo scenario."""
        super().__init__()
        self.setWindowTitle("QGIS 3 Profiling Dashboard")
        self.resize(860, 720)
        self._apply_shell_style()

        root_layout = QVBoxLayout()
        root_layout.setContentsMargins(18, 18, 18, 18)
        root_layout.setSpacing(12)
        self.setLayout(root_layout)

        root_layout.addWidget(self._build_header())
        root_layout.addWidget(self._build_execution_panel())
        root_layout.addWidget(self._build_checks_panel())
        root_layout.addWidget(self._build_logs_panel(), 1)
        root_layout.addLayout(self._build_footer())

        self.load_scenario("success")

    def _apply_shell_style(self):
        """Apply a clean corporate visual style without changing QGIS internals."""
        self.setStyleSheet(
            """
            QDialog {
                background-color: #f4f7fb;
            }
            QFrame#card {
                background-color: #ffffff;
                border: 1px solid #d7e1ea;
                border-radius: 10px;
            }
            QLabel#title {
                font-size: 20px;
                font-weight: 700;
                color: #16324f;
            }
            QLabel#subtitle {
                color: #516577;
                font-size: 11px;
            }
            QLabel#sectionTitle {
                color: #16324f;
                font-size: 13px;
                font-weight: 700;
            }
            QLabel#metaLabel {
                color: #6b7a88;
                font-weight: 600;
            }
            QLabel#metaValue {
                color: #203040;
            }
            QLabel#overallBadge {
                color: #ffffff;
                background-color: #16324f;
                border-radius: 14px;
                padding: 6px 12px;
                font-weight: 700;
            }
            QProgressBar {
                border: 1px solid #d7e1ea;
                border-radius: 6px;
                background: #eef3f8;
                text-align: center;
                min-height: 22px;
                font-weight: 600;
            }
            QTextEdit {
                background-color: #0f1720;
                color: #d7e6f7;
                border: 1px solid #243241;
                border-radius: 8px;
                font-family: Consolas;
                font-size: 11px;
            }
            QPushButton {
                min-height: 32px;
                border-radius: 6px;
                padding: 0 12px;
            }
            QPushButton#primary {
                background-color: #1d5f8c;
                color: white;
                border: none;
                font-weight: 700;
            }
            QPushButton#secondary {
                background-color: #ffffff;
                color: #16324f;
                border: 1px solid #c3d0dc;
            }
            QComboBox {
                min-height: 30px;
                border-radius: 6px;
                border: 1px solid #c3d0dc;
                padding: 0 8px;
                background: #ffffff;
            }
            """
        )

    def _build_header(self) -> QWidget:
        """Build the title area that explains the dashboard purpose to the client."""
        card = self._create_card()
        layout = QVBoxLayout(card)

        title = QLabel("QGIS 3 Profiling and Validation Dashboard")
        title.setObjectName("title")
        subtitle = QLabel(
            "Business readiness view for job checks, layer loading, DBKR/CBB health, "
            "data freshness, polygon validation, and execution trace."
        )
        subtitle.setWordWrap(True)
        subtitle.setObjectName("subtitle")

        layout.addWidget(title)
        layout.addWidget(subtitle)
        return card

    def _build_execution_panel(self) -> QWidget:
        """Build the scenario selector and top-level execution metadata panel."""
        card = self._create_card()
        layout = QGridLayout(card)
        layout.setHorizontalSpacing(14)
        layout.setVerticalSpacing(8)

        section_title = QLabel("Execution Context")
        section_title.setObjectName("sectionTitle")

        self.scenario_box = QComboBox()
        self.scenario_box.addItems(SCENARIOS.keys())
        self.scenario_box.currentTextChanged.connect(self.load_scenario)

        self.job_name_value = QLabel("-")
        self.job_name_value.setObjectName("metaValue")
        self.mode_value = QLabel("-")
        self.mode_value.setObjectName("metaValue")
        self.executed_at_value = QLabel("-")
        self.executed_at_value.setObjectName("metaValue")
        self.log_path_value = QLabel("-")
        self.log_path_value.setObjectName("metaValue")
        self.log_path_value.setWordWrap(True)
        self.overall_badge = QLabel("Overall: -")
        self.overall_badge.setObjectName("overallBadge")

        layout.addWidget(section_title, 0, 0)
        layout.addWidget(self.overall_badge, 0, 1, alignment=Qt.AlignRight)
        layout.addWidget(self._meta_label("Demo Scenario"), 1, 0)
        layout.addWidget(self.scenario_box, 1, 1)
        layout.addWidget(self._meta_label("Job / Context"), 2, 0)
        layout.addWidget(self.job_name_value, 2, 1)
        layout.addWidget(self._meta_label("Execution Mode"), 3, 0)
        layout.addWidget(self.mode_value, 3, 1)
        layout.addWidget(self._meta_label("Executed At"), 4, 0)
        layout.addWidget(self.executed_at_value, 4, 1)
        layout.addWidget(self._meta_label("Log File"), 5, 0)
        layout.addWidget(self.log_path_value, 5, 1)

        return card

    def _build_checks_panel(self) -> QWidget:
        """Build the main status grid with one progress bar per business check."""
        card = self._create_card()
        layout = QVBoxLayout(card)

        section_title = QLabel("Validation Summary")
        section_title.setObjectName("sectionTitle")
        layout.addWidget(section_title)

        grid = QGridLayout()
        grid.setHorizontalSpacing(14)
        grid.setVerticalSpacing(10)
        self.rows = {}

        for index, label_text in enumerate(CHECK_LABELS):
            label = QLabel(label_text)
            label.setObjectName("metaValue")

            bar = QProgressBar()
            bar.setAlignment(Qt.AlignCenter)

            status_label = QLabel("-")
            status_label.setObjectName("metaValue")

            grid.addWidget(label, index, 0)
            grid.addWidget(bar, index, 1)
            grid.addWidget(status_label, index, 2)

            self.rows[label_text] = {"bar": bar, "status": status_label}

        overall_text = QLabel("Overall Status")
        overall_text.setObjectName("metaValue")
        self.overall_bar = QProgressBar()
        self.overall_bar.setAlignment(Qt.AlignCenter)
        self.overall_status_label = QLabel("-")
        self.overall_status_label.setObjectName("metaValue")

        grid.addWidget(overall_text, len(CHECK_LABELS), 0)
        grid.addWidget(self.overall_bar, len(CHECK_LABELS), 1)
        grid.addWidget(self.overall_status_label, len(CHECK_LABELS), 2)

        layout.addLayout(grid)
        return card

    def _build_logs_panel(self) -> QWidget:
        """Build the execution log viewer shown at the bottom of the dialog."""
        card = self._create_card()
        layout = QVBoxLayout(card)

        section_title = QLabel("Execution Log")
        section_title.setObjectName("sectionTitle")
        self.logs = QTextEdit()
        self.logs.setReadOnly(True)

        layout.addWidget(section_title)
        layout.addWidget(self.logs)
        return card

    def _build_footer(self) -> QHBoxLayout:
        """Build footer buttons for refreshing or closing the dashboard."""
        layout = QHBoxLayout()
        layout.addStretch(1)

        refresh_btn = QPushButton("Reload Scenario")
        refresh_btn.setObjectName("secondary")
        refresh_btn.clicked.connect(lambda: self.load_scenario(self.scenario_box.currentText()))

        close_btn = QPushButton("Close")
        close_btn.setObjectName("primary")
        close_btn.clicked.connect(self.close)

        layout.addWidget(refresh_btn)
        layout.addWidget(close_btn)
        return layout

    def _create_card(self) -> QFrame:
        """Create a reusable white card container used across the dashboard."""
        card = QFrame()
        card.setObjectName("card")
        return card

    def _meta_label(self, text: str) -> QLabel:
        """Create a small label used for execution metadata headings."""
        label = QLabel(text)
        label.setObjectName("metaLabel")
        return label

    def _apply_status(self, bar: QProgressBar, status_label: QLabel, value: str):
        """Render one status value as colored progress plus readable text."""
        normalized = value.strip().lower()

        if normalized == "failed":
            bar.setValue(100)
            bar.setFormat("Failed")
            bar.setStyleSheet(self._progress_style("#c0392b"))
            status_label.setText("Business or technical blocker detected")
            return

        if normalized == "slow":
            bar.setValue(70)
            bar.setFormat("Slow")
            bar.setStyleSheet(self._progress_style("#e67e22"))
            status_label.setText("Completed with performance warning")
            return

        percent = int(value.replace("%", ""))
        bar.setValue(percent)
        bar.setFormat(value)
        bar.setStyleSheet(self._progress_style("#2d8f5b"))

        if percent >= 100:
            status_label.setText("Completed successfully")
        elif percent >= 90:
            status_label.setText("Completed with minor concern")
        else:
            status_label.setText("Partial completion")

    def _progress_style(self, color: str) -> str:
        """Generate a consistent progress-bar chunk style for one status color."""
        return (
            "QProgressBar::chunk {"
            f"background-color: {color};"
            "border-radius: 5px;"
            "}"
        )

    def load_scenario(self, scenario_name: str):
        """Load one demo scenario and update all visible dashboard sections."""
        payload = get_scenario_payload(scenario_name)

        self.job_name_value.setText(payload["job_name"])
        self.mode_value.setText(payload["execution_mode"])
        self.executed_at_value.setText(payload["logs"][0].split(" - ")[0].lstrip("-"))
        self.log_path_value.setText(payload["log_path"])
        self.overall_badge.setText(f"Overall: {payload['overall']}")

        for label_text, widgets in self.rows.items():
            self._apply_status(widgets["bar"], widgets["status"], payload["checks"][label_text])

        self._apply_status(self.overall_bar, self.overall_status_label, payload["overall"])
        self.logs.setPlainText("\n".join(payload["logs"]))


def launch_dashboard():
    """Start the dashboard in a normal Qt application for local demo use."""
    app = QApplication.instance() or QApplication([])
    dialog = QGISProfileReportDialog()
    dialog.show()
    return app, dialog
