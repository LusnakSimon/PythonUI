"""
5. Textual — Modern Terminal User Interface (TUI) with CSS Styling & Mouse Support
Install: pip install textual
Run:     python 05_textual_tui_app.py
"""

from textual.app import App, ComposeResult
from textual.containers import Container, Horizontal, Vertical
from textual.widgets import Button, Footer, Header, Input, Label, ProgressBar, RichLog, Static


class MetricCard(Static):
    def __init__(self, title: str, value: str, sub: str) -> None:
        super().__init__()
        self.card_title = title
        self.card_value = value
        self.card_sub = sub

    def compose(self) -> ComposeResult:
        yield Label(self.card_title, classes="metric-title")
        yield Label(self.card_value, classes="metric-value")
        yield Label(self.card_sub, classes="metric-sub")


class ModernTUIApp(App):
    TITLE = "NovaUI — Textual TUI"
    CSS = """
    Screen {
        background: #0f172a;
        color: #f8fafc;
    }
    #sidebar {
        width: 24;
        background: #1e293b;
        border-right: solid #334155;
        padding: 1 2;
    }
    #logo {
        text-style: bold;
        color: #38bdf8;
        margin-bottom: 1;
    }
    .nav-btn {
        width: 100%;
        margin-bottom: 1;
        border: none;
    }
    #main {
        padding: 1 2;
    }
    #page-title {
        text-style: bold;
        color: #f8fafc;
        margin-bottom: 1;
    }
    #metrics-row {
        height: 7;
        margin-bottom: 1;
    }
    MetricCard {
        width: 1fr;
        background: #1e293b;
        border: round #334155;
        padding: 0 2;
        margin-right: 1;
    }
    .metric-title {
        color: #94a3b8;
    }
    .metric-value {
        text-style: bold;
        color: #ffffff;
    }
    .metric-sub {
        color: #34d399;
    }
    #workspace {
        background: #1e293b;
        border: round #334155;
        padding: 1 2;
        height: 1fr;
    }
    #input-row {
        height: 3;
        margin-top: 1;
    }
    #task-input {
        width: 1fr;
    }
    RichLog {
        background: #0f172a;
        border: round #334155;
        margin-top: 1;
        height: 1fr;
    }
    """

    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)
        with Horizontal():
            with Vertical(id="sidebar"):
                yield Label("⚡ NovaUI", id="logo")
                for idx, name in enumerate(["Dashboard", "Analytics", "Projects", "Settings"]):
                    yield Button(
                        name,
                        id=f"nav-{name.lower()}",
                        variant="primary" if idx == 0 else "default",
                        classes="nav-btn",
                    )
            with Vertical(id="main"):
                yield Label("Dashboard", id="page-title")
                with Horizontal(id="metrics-row"):
                    yield MetricCard("Active Tasks", "24", "+12% this week")
                    yield MetricCard("System Load", "38%", "Optimal performance")
                    yield MetricCard("Completed", "142", "98.4% success rate")
                with Container(id="workspace"):
                    yield Label("Quick Task Runner")
                    with Horizontal(id="input-row"):
                        yield Input(placeholder="Enter a command or note...", id="task-input")
                        yield Button("Run Action", id="run-btn", variant="primary")
                    pbar = ProgressBar(total=100, show_eta=False)
                    pbar.advance(65)
                    yield pbar
                    yield RichLog(id="log-box", highlight=True)
        yield Footer()

    def on_mount(self) -> None:
        log = self.query_one("#log-box", RichLog)
        log.write("✅ Environment initialized.")
        log.write("✅ Ready for input...")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        btn_id = event.button.id or ""
        if btn_id.startswith("nav-"):
            page_name = str(event.button.label)
            self.query_one("#page-title", Label).update(page_name)
            for b in self.query(".nav-btn"):
                b.variant = "primary" if b.id == btn_id else "default"
        elif btn_id == "run-btn":
            self._execute_task()

    def on_input_submitted(self, event: Input.Submitted) -> None:
        if event.input.id == "task-input":
            self._execute_task()

    def _execute_task(self) -> None:
        inp = self.query_one("#task-input", Input)
        text = inp.value.strip()
        if text:
            self.query_one("#log-box", RichLog).write(f"▶ Executed: {text}")
            inp.value = ""


if __name__ == "__main__":
    ModernTUIApp().run()
