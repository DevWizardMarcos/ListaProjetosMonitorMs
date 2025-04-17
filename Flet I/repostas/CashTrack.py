import flet as ft

def main(page: ft.Page):
    page.title = "CashTrack - Controle Financeiro"
    page.scroll = "auto"

    saldo = 0.0
    lancamentos = []

    # Campo de entrada
    descricao_input = ft.TextField(label="Descrição", width=300)
    valor_input = ft.TextField(label="Valor", width=150)
    tipo_input = ft.Dropdown(
        width=150,
        label="Tipo",
        options=[
            ft.dropdown.Option("Receita"),
            ft.dropdown.Option("Despesa")
        ]
    )

    lista_lancamentos = ft.Column()
    saldo_text = ft.Text(f"💰 Saldo Atual: R$ {saldo:.2f}", size=22, weight="bold", color=ft.colors.GREEN)

    def atualizar_saldo():
        total = 0
        for item in lancamentos:
            if item["tipo"] == "Receita":
                total += item["valor"]
            else:
                total -= item["valor"]
        saldo_text.value = f"💰 Saldo Atual: R$ {total:.2f}"
        saldo_text.color = ft.colors.GREEN if total >= 0 else ft.colors.RED
        page.update()

    def adicionar_lancamento(e):
        try:
            valor = float(valor_input.value)
            tipo = tipo_input.value
            descricao = descricao_input.value

            if not tipo or not descricao:
                raise ValueError("Campos incompletos")

            lancamentos.append({"descricao": descricao, "valor": valor, "tipo": tipo})

            cor = ft.colors.GREEN if tipo == "Receita" else ft.colors.RED
            prefixo = "+" if tipo == "Receita" else "-"

            item = ft.Text(f"{descricao}: {prefixo}R$ {valor:.2f} [{tipo}]", color=cor, size=16)
            lista_lancamentos.controls.append(item)

            atualizar_saldo()
            descricao_input.value = ""
            valor_input.value = ""
            tipo_input.value = ""
            page.update()

        except ValueError:
            page.snack_bar = ft.SnackBar(ft.Text("Por favor, preencha todos os campos corretamente!", color="white"))
            page.snack_bar.open = True
            page.update()

    # Layout principal
    page.add(
        ft.Text("📊 CashTrack - Seu controle financeiro simples", size=26, weight="bold"),
        ft.Row([descricao_input, valor_input, tipo_input]),
        ft.ElevatedButton("Adicionar Lançamento", on_click=adicionar_lancamento),
        saldo_text,
        ft.Divider(),
        ft.Text("📋 Histórico de Lançamentos:", size=20, weight="bold"),
        lista_lancamentos
    )

ft.app(target=main)
