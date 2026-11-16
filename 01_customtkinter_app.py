"""
1. CustomTkinter — Modernized Tkinter Desktop UI
Install: pip install customtkinter
Run:     python 01_customtkinter_app.py
"""

import customtkinter as ctk

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")


class ModernCTkApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("NovaUI — CustomTkinter")
        self.geometry("920x580")
        self.minsize(760, 480)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self._build_sidebar()
        self._build_main_view()

    def _build_sidebar(self):
        self.sidebar = ctk.CTkFrame(self, width=210, corner_radius=0)
        self.sidebar.grid(row=0, column=0, sticky="nsew")
        self.sidebar.grid_rowconfigure(5, weight=1)

        ctk.CTkLabel(
            self.sidebar,
            text="⚡ NovaUI",
            font=ctk.CTkFont(size=22, weight="bold"),
        ).grid(row=0, column=0, padx=20, pady=(24, 20), sticky="w")

        nav_items = ["Dashboard", "Analytics", "Projects", "Settings"]
        self.nav_buttons = []
        for idx, name in enumerate(nav_items, start=1):
            btn = ctk.CTkButton(
                self.sidebar,
                text=name,
                corner_radius=8,
                height=38,
                anchor="w",
                fg_color=("#3B8ED0", "#1F6AA5") if idx == 1 else "transparent",
                text_color=("gray10", "gray90"),
                hover_color=("gray75", "gray25"),
                command=lambda n=name: self.select_nav(n),
            )
            btn.grid(row=idx, column=0, padx=16, pady=4, sticky="ew")
            self.nav_buttons.append((name, btn))

        ctk.CTkLabel(self.sidebar, text="Theme Mode", anchor="w").grid(
            row=6, column=0, padx=20, pady=(10, 0), sticky="w"
        )
        self.theme_menu = ctk.CTkOptionMenu(
            self.sidebar,
            values=["Dark", "Light", "System"],
            command=ctk.set_appearance_mode,
        )
        self.theme_menu.grid(row=7, column=0, padx=20, pady=(6, 24), sticky="ew")

    def _build_main_view(self):
        self.main_frame = ctk.CTkFrame(self, corner_radius=12, fg_color="transparent")
        self.main_frame.grid(row=0, column=1, padx=24, pady=24, sticky="nsew")
        self.main_frame.grid_columnconfigure((0, 1, 2), weight=1)
        self.main_frame.grid_rowconfigure(2, weight=1)

        self.header_label = ctk.CTkLabel(
            self.main_frame,
            text="Dashboard",
            font=ctk.CTkFont(size=26, weight="bold"),
        )
        self.header_label.grid(row=0, column=0, columnspan=2, pady=(0, 20), sticky="w")

        self.search_entry = ctk.CTkEntry(
            self.main_frame,
            placeholder_text="Search tasks or projects...",
            height=36,
            corner_radius=8,
        )
        self.search_entry.grid(row=0, column=2, pady=(0, 20), sticky="ew")

        metrics = [
            ("Active Tasks", "24", "+12% this week"),
            ("System Load", "38%", "Optimal performance"),
            ("Completed", "142", "98.4% success rate"),
        ]
        for col, (title, value, sub) in enumerate(metrics):
            card = ctk.CTkFrame(self.main_frame, corner_radius=12)
            card.grid(
                row=1,
                column=col,
                padx=(0 if col == 0 else 8, 0 if col == 2 else 8),
                pady=(0, 20),
                sticky="nsew",
            )
            ctk.CTkLabel(card, text=title, text_color="gray", font=ctk.CTkFont(size=13)).pack(
                anchor="w", padx=16, pady=(14, 2)
            )
            ctk.CTkLabel(card, text=value, font=ctk.CTkFont(size=28, weight="bold")).pack(
                anchor="w", padx=16
            )
            ctk.CTkLabel(card, text=sub, text_color="#2FA572", font=ctk.CTkFont(size=12)).pack(
                anchor="w", padx=16, pady=(2, 14)
            )

        self.workspace = ctk.CTkFrame(self.main_frame, corner_radius=12)
        self.workspace.grid(row=2, column=0, columnspan=3, sticky="nsew")
        self.workspace.grid_columnconfigure(0, weight=1)
        self.workspace.grid_rowconfigure(3, weight=1)

        ctk.CTkLabel(
            self.workspace,
            text="Quick Task Runner",
            font=ctk.CTkFont(size=16, weight="bold"),
        ).grid(row=0, column=0, padx=20, pady=(18, 10), sticky="w")

        self.task_input = ctk.CTkEntry(
            self.workspace,
            placeholder_text="Enter a command or note...",
            height=40,
        )
        self.task_input.grid(row=1, column=0, padx=(20, 10), pady=8, sticky="ew")
        self.task_input.bind("<Return>", lambda _: self.run_action())

        self.run_btn = ctk.CTkButton(
            self.workspace,
            text="Run Action",
            height=40,
            corner_radius=8,
            command=self.run_action,
        )
        self.run_btn.grid(row=1, column=1, padx=(0, 20), pady=8)

        self.progress = ctk.CTkProgressBar(self.workspace)
        self.progress.grid(row=2, column=0, columnspan=2, padx=20, pady=(12, 8), sticky="ew")
        self.progress.set(0.65)

        self.log_box = ctk.CTkTextbox(self.workspace, corner_radius=8, height=160)
        self.log_box.grid(row=3, column=0, columnspan=2, padx=20, pady=(8, 20), sticky="nsew")
        self.log_box.insert("0.0", "✅ Environment initialized.\n✅ Ready for input...\n")

    def select_nav(self, selected_name: str):
        self.header_label.configure(text=selected_name)
        for name, btn in self.nav_buttons:
            btn.configure(
                fg_color=("#3B8ED0", "#1F6AA5") if name == selected_name else "transparent"
            )

    def run_action(self):
        text = self.task_input.get().strip()
        if text:
            self.log_box.insert("end", f"▶ Executed: {text}\n")
            self.log_box.see("end")
            self.task_input.delete(0, "end")


if __name__ == "__main__":
    app = ModernCTkApp()
    app.mainloop()
