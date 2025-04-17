import flet as ft

def main(page: ft.Page):
    page.title = "Dashboard de Produtividade"
    page.bgcolor = "#f0f2f5"
    page.scroll = "auto"
    page.horizontal_alignment = "center"

    def on_hover_card(e):
        e.control.elevation = 10 if e.data == "true" else 2
        e.control.update()

    def on_click_card(e):
        colors = ["#c8e6c9", "#bbdefb", "#ffe0b2", "#f8bbd0"]
        import random
        e.control.bgcolor = random.choice(colors)
        e.control.update()

    def criar_card(titulo, progresso):
        return ft.Container(
            width=300,
            height=200,
            bgcolor="#ffffff",
            border_radius=15,
            elevation=2,
            padding=20,
            animate_elevation=True,
            animate_bgcolor=True,
            on_hover=on_hover_card,
            on_click=on_click_card,
            shadow=ft.BoxShadow(
                blur_radius=6,
                color="grey",
                offset=ft.Offset(2,2)
            ),
            content=ft.Column([
                ft.Text(titulo, size=20, weight="bold", color="#333333"),
                ft.ProgressBar(value=progresso, bgcolor="#eeeeee", color="#00c853"),
            ],
            alignment="center",
            horizontal_alignment="center"
            ),
        )

    dashboard = ft.Row([
        criar_card("Tarefas", 0.7),
        criar_card("Hábitos", 0.5),
        criar_card("Projetos", 0.3),
    ], alignment="center", wrap=True)

    page.add(dashboard)

ft.app(target=main)
