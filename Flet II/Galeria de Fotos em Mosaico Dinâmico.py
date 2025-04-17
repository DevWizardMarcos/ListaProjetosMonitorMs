import flet as ft

def main(page: ft.Page):
    page.title = "Galeria de Fotos"
    page.scroll = "auto"
    page.bgcolor = "#f0f0f0"

    imagens = [
        "https://picsum.photos/200/200?1",
        "https://picsum.photos/200/200?2",
        "https://picsum.photos/200/200?3",
        "https://picsum.photos/200/200?4",
    ]

    foto_controles = []

    def criar_foto(url):
        img = ft.Container(
            width=150,
            height=150,
            border_radius=10,
            bgcolor="#ffffff",
            margin=5,
            content=ft.Image(src=url, fit="cover"),
            animate_scale=True,
            on_hover=lambda e: (setattr(e.control, "scale", 1.05) if e.data == "true" else setattr(e.control, "scale", 1), e.control.update()),
        )
        return ft.Draggable(
            group="fotos",
            content=img,
            content_when_dragging=img,
            feedback=img,
        )

    def atualizar_galeria():
        page.controls.clear()
        page.add(
            ft.Wrap(
                [criar_foto(url) for url in imagens],
                run_spacing=10,
                spacing=10,
                alignment="center",
            )
        )
        page.update()

    atualizar_galeria()

ft.app(target=main)
