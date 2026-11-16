"""
3. Flet — Flutter / Material 3 UI for Python (Desktop, Web & Mobile)
Install: pip install flet
Run:     python 03_flet_app.py
"""

import flet as ft


def main(page: ft.Page):
    page.title = "NovaUI — Flet (Flutter for Python)"
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 0
    page.window.width = 940
    page.window.height = 600
    page.bgcolor = "#0f172a"

    header_text = ft.Text("Dashboard", size=26, weight=ft.FontWeight.BOLD)
    log_column = ft.Column(
        controls=[
            ft.Text("✅ Environment initialized.", font_family="Consolas", size=13, color="#94a3b8"),
            ft.Text("✅ Ready for input...", font_family="Consolas", size=13, color="#94a3b8"),
        ],
        scroll=ft.ScrollMode.AUTO,
        expand=True,
    )
    task_input = ft.TextField(
        hint_text="Enter a command or note...",
        expand=True,
        border_radius=8,
        bgcolor="#0f172a",
        border_color="#334155",
    )

    def run_action(e):
        if task_input.value and task_input.value.strip():
            log_column.controls.append(
                ft.Text(f"▶ Executed: {task_input.value.strip()}", font_family="Consolas", size=13)
            )
            task_input.value = ""
            page.update()

    task_input.on_submit = run_action

    nav_destinations = ["Dashboard", "Analytics", "Projects", "Settings"]

    def on_nav_change(e):
        header_text.value = nav_destinations[e.control.selected_index]
        page.update()

    rail = ft.NavigationRail(
        selected_index=0,
        label_type=ft.NavigationRailLabelType.ALL,
        min_width=100,
        min_extended_width=200,
        extended=True,
        bgcolor="#1e293b",
        leading=ft.Container(
            content=ft.Text("⚡ NovaUI", size=20, weight=ft.FontWeight.BOLD, color="#38bdf8"),
            padding=ft.padding.only(top=20, bottom=16, left=12),
        ),
        destinations=[
            ft.NavigationRailDestination(icon=ft.Icons.DASHBOARD_OUTLINED, selected_icon=ft.Icons.DASHBOARD, label="Dashboard"),
            ft.NavigationRailDestination(icon=ft.Icons.ANALYTICS_OUTLINED, selected_icon=ft.Icons.ANALYTICS, label="Analytics"),
            ft.NavigationRailDestination(icon=ft.Icons.FOLDER_OUTLINED, selected_icon=ft.Icons.FOLDER, label="Projects"),
            ft.NavigationRailDestination(icon=ft.Icons.SETTINGS_OUTLINED, selected_icon=ft.Icons.SETTINGS, label="Settings"),
        ],
        on_change=on_nav_change,
    )

    def metric_card(title: str, value: str, sub: str):
        return ft.Container(
            expand=True,
            padding=18,
            border_radius=12,
            bgcolor="#1e293b",
            border=ft.border.all(1, "#334155"),
            content=ft.Column(
                spacing=4,
                controls=[
                    ft.Text(title, size=13, color="#94a3b8"),
                    ft.Text(value, size=28, weight=ft.FontWeight.BOLD),
                    ft.Text(sub, size=12, color="#34d399"),
                ],
            ),
        )

    main_content = ft.Container(
        expand=True,
        padding=28,
        content=ft.Column(
            spacing=20,
            expand=True,
            controls=[
                # Header Row
                ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        header_text,
                        ft.TextField(
                            hint_text="Search tasks or projects...",
                            width=250,
                            height=42,
                            content_padding=10,
                            border_radius=8,
                            bgcolor="#1e293b",
                            border_color="#334155",
                        ),
                    ],
                ),
                # Metric Cards Row
                ft.Row(
                    spacing=16,
                    controls=[
                        metric_card("Active Tasks", "24", "+12% this week"),
                        metric_card("System Load", "38%", "Optimal performance"),
                        metric_card("Completed", "142", "98.4% success rate"),
                    ],
                ),
                # Interactive Workspace Card
                ft.Container(
                    expand=True,
                    padding=20,
                    border_radius=12,
                    bgcolor="#1e293b",
                    border=ft.border.all(1, "#334155"),
                    content=ft.Column(
                        spacing=12,
                        expand=True,
                        controls=[
                            ft.Text("Quick Task Runner", size=16, weight=ft.FontWeight.BOLD),
                            ft.Row(
                                controls=[
                                    task_input,
                                    ft.FilledButton(
                                        "Run Action",
                                        height=46,
                                        on_click=run_action,
                                    ),
                                ]
                            ),
                            ft.ProgressBar(value=0.65, color="#38bdf8", bgcolor="#0f172a"),
                            ft.Container(
                                expand=True,
                                padding=12,
                                border_radius=8,
                                bgcolor="#0f172a",
                                border=ft.border.all(1, "#334155"),
                                content=log_column,
                            ),
                        ],
                    ),
                ),
            ],
        ),
    )

    page.add(ft.Row([rail, main_content], expand=True, spacing=0))


if __name__ == "__main__":
    ft.app(target=main)
