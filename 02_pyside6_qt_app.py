"""
2. PySide6 (Qt6) — Professional Native Desktop UI with Modern QSS Styling
Install: pip install PySide6
Run:     python 02_pyside6_qt_app.py
"""

import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QFrame,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMainWindow,
    QProgressBar,
    QPushButton,
    QTextEdit,
    QVBoxLayout,
    QWidget,
)

MODERN_DARK_QSS = """
QMainWindow {
    background-color: #0f172a;
}
QWidget {
    color: #f8fafc;
    font-family: 'Segoe UI', 'Inter', sans-serif;
    font-size: 14px;
}
#Sidebar {
    background-color: #1e293b;
    border-right: 1px solid #334155;
}
#Logo {
    font-size: 22px;
    font-weight: bold;
    color: #38bdf8;
    padding: 8px 4px;
}
QPushButton.NavBtn {
    background-color: transparent;
    border: none;
    border-radius: 8px;
    padding: 10px 14px;
    text-align: left;
    color: #cbd5e1;
    font-weight: 500;
}
QPushButton.NavBtn:hover {
    background-color: #334155;
    color: #ffffff;
}
QPushButton.NavBtn[active="true"] {
    background-color: #0284c7;
    color: #ffffff;
    font-weight: 600;
}
QFrame.Card {
    background-color: #1e293b;
    border: 1px solid #334155;
    border-radius: 12px;
}
QLineEdit {
    background-color: #0f172a;
    border: 1px solid #334155;
    border-radius: 8px;
    padding: 8px 12px;
    color: #f8fafc;
}
QLineEdit:focus {
    border: 1px solid #38bdf8;
}
QPushButton#ActionBtn {
    background-color: #0284c7;
    border: none;
    border-radius: 8px;
    padding: 10px 20px;
    font-weight: 600;
    color: white;
}
QPushButton#ActionBtn:hover {
    background-color: #0369a1;
}
QProgressBar {
    background-color: #0f172a;
    border: none;
    border-radius: 5px;
    height: 10px;
    text-align: center;
}
QProgressBar::chunk {
    background-color: #38bdf8;
    border-radius: 5px;
}
QTextEdit {
    background-color: #0f172a;
    border: 1px solid #334155;
    border-radius: 8px;
    padding: 10px;
    font-family: 'Cascadia Code', 'Consolas', monospace;
    font-size: 13px;
}
"""


class ModernQtApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("NovaUI — PySide6 (Qt6)")
        self.resize(920, 580)
        self.setMinimumSize(760, 480)

        root = QWidget()
        self.setCentralWidget(root)
        main_layout = QHBoxLayout(root)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        main_layout.addWidget(self._build_sidebar())
        main_layout.addWidget(self._build_content(), stretch=1)

    def _build_sidebar(self):
        sidebar = QFrame()
        sidebar.setObjectName("Sidebar")
        sidebar.setFixedWidth(210)
        layout = QVBoxLayout(sidebar)
        layout.setContentsMargins(16, 24, 16, 24)
        layout.setSpacing(6)

        logo = QLabel("⚡ NovaUI")
        logo.setObjectName("Logo")
        layout.addWidget(logo)
        layout.addSpacing(12)

        self.nav_buttons = []
        for idx, name in enumerate(["Dashboard", "Analytics", "Projects", "Settings"]):
            btn = QPushButton(name)
            btn.setProperty("class", "NavBtn")
            btn.setProperty("active", "true" if idx == 0 else "false")
            btn.setCursor(Qt.PointingHandCursor)
            btn.clicked.connect(lambda checked=False, n=name: self.select_nav(n))
            layout.addWidget(btn)
            self.nav_buttons.append((name, btn))

        layout.addStretch()
        footer = QLabel("Qt6 QSS Engine")
        footer.setStyleSheet("color: #64748b; font-size: 12px; padding-left: 6px;")
        layout.addWidget(footer)
        return sidebar

    def _build_content(self):
        content = QWidget()
        layout = QVBoxLayout(content)
        layout.setContentsMargins(28, 24, 28, 24)
        layout.setSpacing(20)

        # Header row
        header_row = QHBoxLayout()
        self.header_label = QLabel("Dashboard")
        self.header_label.setStyleSheet("font-size: 26px; font-weight: bold;")
        header_row.addWidget(self.header_label)
        header_row.addStretch()

        search = QLineEdit()
        search.setPlaceholderText("Search tasks or projects...")
        search.setFixedWidth(250)
        header_row.addWidget(search)
        layout.addLayout(header_row)

        # Metric cards row
        cards_row = QHBoxLayout()
        cards_row.setSpacing(16)
        metrics = [
            ("Active Tasks", "24", "+12% this week"),
            ("System Load", "38%", "Optimal performance"),
            ("Completed", "142", "98.4% success rate"),
        ]
        for title, value, sub in metrics:
            card = QFrame()
            card.setProperty("class", "Card")
            c_layout = QVBoxLayout(card)
            c_layout.setContentsMargins(18, 16, 18, 16)

            lbl_title = QLabel(title)
            lbl_title.setStyleSheet("color: #94a3b8; font-size: 13px;")
            lbl_val = QLabel(value)
            lbl_val.setStyleSheet("font-size: 28px; font-weight: bold; margin: 4px 0;")
            lbl_sub = QLabel(sub)
            lbl_sub.setStyleSheet("color: #34d399; font-size: 12px;")

            c_layout.addWidget(lbl_title)
            c_layout.addWidget(lbl_val)
            c_layout.addWidget(lbl_sub)
            cards_row.addWidget(card)
        layout.addLayout(cards_row)

        # Workspace card
        workspace = QFrame()
        workspace.setProperty("class", "Card")
        w_layout = QVBoxLayout(workspace)
        w_layout.setContentsMargins(20, 20, 20, 20)
        w_layout.setSpacing(12)

        w_title = QLabel("Quick Task Runner")
        w_title.setStyleSheet("font-size: 16px; font-weight: bold;")
        w_layout.addWidget(w_title)

        input_row = QHBoxLayout()
        self.task_input = QLineEdit()
        self.task_input.setPlaceholderText("Enter a command or note...")
        self.task_input.returnPressed.connect(self.run_action)
        run_btn = QPushButton("Run Action")
        run_btn.setObjectName("ActionBtn")
        run_btn.setCursor(Qt.PointingHandCursor)
        run_btn.clicked.connect(self.run_action)
        input_row.addWidget(self.task_input, stretch=1)
        input_row.addWidget(run_btn)
        w_layout.addLayout(input_row)

        progress = QProgressBar()
        progress.setValue(65)
        progress.setTextVisible(False)
        w_layout.addWidget(progress)

        self.log_box = QTextEdit()
        self.log_box.setReadOnly(True)
        self.log_box.setPlainText("✅ Environment initialized.\n✅ Ready for input...")
        w_layout.addWidget(self.log_box, stretch=1)

        layout.addWidget(workspace, stretch=1)
        return content

    def select_nav(self, selected_name: str):
        self.header_label.setText(selected_name)
        for name, btn in self.nav_buttons:
            btn.setProperty("active", "true" if name == selected_name else "false")
            btn.style().unpolish(btn)
            btn.style().polish(btn)

    def run_action(self):
        text = self.task_input.text().strip()
        if text:
            self.log_box.append(f"▶ Executed: {text}")
            self.task_input.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet(MODERN_DARK_QSS)
    window = ModernQtApp()
    window.show()
    sys.exit(app.exec())
