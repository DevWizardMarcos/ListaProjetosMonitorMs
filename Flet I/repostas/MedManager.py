import flet as ft
from datetime import datetime

# Lista para armazenar os lembretes
lembretes = []

def main(page: ft.Page):
    page.title = "💊 MedManager - Lembrete de Medicamentos"
    page.scroll = "auto"
    page.vertical_alignment = ft.MainAxisAlignment.START

    nome_input = ft.TextField(label="Nome do Medicamento", width=300)
    hora_input = ft.TextField(label="Horário (HH:MM)", width=150)
    dose_input = ft.TextField(label="Dose", width=150)
    lista_lembretes = ft.Column()

    def adicionar_lembrete(e):
        nome = nome_input.value.strip()
        hora = hora_input.value.strip()
        dose = dose_input.value.strip()

        if not nome or not hora or not dose:
            page.snack_bar = ft.SnackBar(ft.Text("⚠️ Preencha todos os campos!", color="white"), bgcolor="red")
            page.snack_bar.open = True
            page.update()
            return

        try:
            hora_obj = datetime.strptime(hora, "%H:%M")
        except ValueError:
            page.snack_bar = ft.SnackBar(ft.Text("⏰ Horário inválido! Use o formato HH:MM", color="white"), bgcolor="orange")
            page.snack_bar.open = True
            page.update()
            return

        lembrete = {
            "nome": nome,
            "hora": hora_obj,
            "dose": dose
        }
        lembretes.append(lembrete)
        atualizar_lista()

        # Limpa campos
        nome_input.value = ""
        hora_input.value = ""
        dose_input.value = ""
        page.update()

    def atualizar_lista():
        lista_lembretes.controls.clear()
        agora = datetime.now()

        for l in sorted(lembretes, key=lambda x: x["hora"]):
            tempo = l["hora"].strftime("%H:%M")
            status = ""

            # Comparação de horário
            if l["hora"].hour == agora.hour and abs(l["hora"].minute - agora.minute) <= 5:
                status = "⏰ AGORA"
                cor = ft.colors.RED
            elif l["hora"] > agora:
                status = "📌 Em breve"
                cor = ft.colors.GREEN
            else:
                status = "✔️ Já passou"
                cor = ft.colors.GREY

            lista_lembretes.controls.append(
                ft.Container(
                    content=ft.Text(f"{l['nome']} - {tempo} - Dose: {l['dose']} - {status}", color=cor),
                    padding=10,
                    border_radius=10,
                    bgcolor="#f1f1f1",
                )
            )
        page.update()

    page.add(
        ft.Text("💊 MedManager - Gerenciador de Lembretes de Remédio", size=24, weight="bold"),
        ft.Row([nome_input, hora_input, dose_input]),
        ft.ElevatedButton("➕ Adicionar Lembrete", on_click=adicionar_lembrete),
        ft.Divider(),
        lista_lembretes
    )

ft.app(target=main)
