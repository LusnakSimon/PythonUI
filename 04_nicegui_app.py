"""
4. NiceGUI — Modern Web & Desktop UI (Vue/Quasar + Tailwind CSS in pure Python)
Install: pip install nicegui
Run:     python 04_nicegui_app.py
"""

from nicegui import ui


@ui.page("/")
def index():
    ui.dark_mode().enable()
    ui.query("body").style("background-color: #0f172a; color: #f8fafc; margin: 0;")

    with ui.row().classes("w-full h-screen no-wrap gap-0"):
        # Left Sidebar
        with ui.column().classes("w-56 h-full bg-slate-800 border-r border-slate-700 p-5 justify-between"):
            with ui.column().classes("w-full gap-2"):
                ui.label("⚡ NovaUI").classes("text-xl font-bold text-sky-400 mb-4 px-2")

                nav_buttons = {}

                def select_nav(name: str):
                    header_label.set_text(name)
                    for btn_name, btn in nav_buttons.items():
                        if btn_name == name:
                            btn.classes(replace="w-full justify-start bg-sky-600 text-white rounded-lg")
                        else:
                            btn.classes(replace="w-full justify-start text-slate-300 hover:bg-slate-700 rounded-lg")

                for idx, item in enumerate(["Dashboard", "Analytics", "Projects", "Settings"]):
                    btn = ui.button(item, on_click=lambda n=item: select_nav(n)).props("flat no-caps")
                    if idx == 0:
                        btn.classes("w-full justify-start bg-sky-600 text-white rounded-lg")
                    else:
                        btn.classes("w-full justify-start text-slate-300 hover:bg-slate-700 rounded-lg")
                    nav_buttons[item] = btn

            ui.label("Tailwind + Quasar UI").classes("text-xs text-slate-400 px-2")

        # Main Content Area
        with ui.column().classes("flex-1 h-full p-7 gap-6 overflow-auto"):
            # Header Row
            with ui.row().classes("w-full items-center justify-between"):
                header_label = ui.label("Dashboard").classes("text-2xl font-bold")
                ui.input(placeholder="Search tasks or projects...").props("outlined dense dark").classes(
                    "w-64 bg-slate-800 rounded-lg"
                )

            # Metric Cards Row
            metrics = [
                ("Active Tasks", "24", "+12% this week"),
                ("System Load", "38%", "Optimal performance"),
                ("Completed", "142", "98.4% success rate"),
            ]
            with ui.row().classes("w-full gap-4"):
                for title, value, sub in metrics:
                    with ui.card().classes(
                        "flex-1 bg-slate-800 border border-slate-700 rounded-xl p-4 shadow-none"
                    ):
                        ui.label(title).classes("text-slate-400 text-sm")
                        ui.label(value).classes("text-3xl font-bold my-1")
                        ui.label(sub).classes("text-emerald-400 text-xs")

            # Interactive Workspace Card
            with ui.card().classes(
                "w-full flex-1 bg-slate-800 border border-slate-700 rounded-xl p-5 shadow-none flex flex-col gap-3"
            ):
                ui.label("Quick Task Runner").classes("text-base font-bold")

                def run_action():
                    text = (task_input.value or "").strip()
                    if text:
                        log_view.push(f"▶ Executed: {text}")
                        task_input.value = ""

                with ui.row().classes("w-full items-center gap-3"):
                    task_input = (
                        ui.input(placeholder="Enter a command or note...")
                        .props("outlined dense dark")
                        .classes("flex-1 bg-slate-900 rounded-lg")
                        .on("keydown.enter", run_action)
                    )
                    ui.button("Run Action", on_click=run_action).props("no-caps").classes(
                        "bg-sky-600 text-white px-5 py-2 rounded-lg font-semibold"
                    )

                ui.linear_progress(value=0.65, show_value=False).props("color=light-blue-4").classes("rounded")

                log_view = ui.log().classes(
                    "w-full flex-1 bg-slate-900 border border-slate-700 rounded-lg p-3 font-mono text-xs text-slate-300"
                )
                log_view.push("✅ Environment initialized.")
                log_view.push("✅ Ready for input...")


if __name__ in {"__main__", "__mp_main__"}:
    ui.run(title="NovaUI — NiceGUI", width=940, height=600, reload=False)
