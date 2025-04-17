import flet as ft

def main(page: ft.Page):
    page.title = "FoodSaver - Desperdício Zero"
    page.theme_mode = "light"
    page.vertical_alignment = ft.MainAxisAlignment.START

    title = ft.Text("FoodSaver - Cadastre e Compartilhe Alimentos", size=24, weight="bold")
    subtitle = ft.Text("Evite o desperdício! Compartilhe alimentos que não vai usar e encontre o que precisa.", size=14)

    food_name = ft.TextField(label="Nome do alimento", width=300)
    quantity = ft.TextField(label="Quantidade / Observações", width=300)
    location = ft.TextField(label="Local (bairro ou região)", width=300)
    share_button = ft.ElevatedButton("Cadastrar alimento", icon=ft.icons.ADD)

    shared_items = ft.Column(auto_scroll=True)

    def add_food(e):
        if food_name.value.strip() and quantity.value.strip() and location.value.strip():
            shared_items.controls.append(
                ft.Card(
                    content=ft.ListTile(
                        title=ft.Text(food_name.value, weight="bold"),
                        subtitle=ft.Text(f"{quantity.value}\nLocal: {location.value}"),
                        leading=ft.Icon(ft.icons.FOOD_BANK, color=ft.colors.GREEN),
                    )
                )
            )
            food_name.value = ""
            quantity.value = ""
            location.value = ""
            page.update()
        else:
            page.snack_bar = ft.SnackBar(ft.Text("Preencha todos os campos!"))
            page.snack_bar.open = True
            page.update()

    share_button.on_click = add_food

    form = ft.Column([
        food_name,
        quantity,
        location,
        share_button
    ], spacing=10)

    page.add(title, subtitle, form, ft.Divider(), ft.Text("Alimentos Compartilhados:", size=18, weight="bold"), shared_items)

ft.app(target=main)
