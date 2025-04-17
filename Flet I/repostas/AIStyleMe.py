import flet as ft
import random

# Estilos baseados em humor + ocasião + estação
recomendacoes = {
    "trabalho": {
        "feliz": {
            "verão": ["Camisa branca de linho + calça bege + mocassim"],
            "inverno": ["Suéter azul-marinho + calça preta + bota de couro"]
        },
        "neutro": {
            "verão": ["Blusa leve azul + saia midi + sapatilha"],
            "inverno": ["Camisa cinza + blazer + jeans escuro"]
        },
        "triste": {
            "verão": ["Camiseta amarela + calça clara + tênis branco"],
            "inverno": ["Cardigan aconchegante + cachecol + jeans"]
        }
    },
    "festa": {
        "feliz": {
            "verão": ["Vestido floral + sandália nude + bolsa pequena"],
            "inverno": ["Jaqueta de couro + saia de vinil + bota"]
        },
        "neutro": {
            "verão": ["Macacão listrado + salto médio + clutch"],
            "inverno": ["Vestido longo com brilho + casaco felpudo"]
        },
        "triste": {
            "verão": ["Blusa neon + jeans rasgado + tênis colorido"],
            "inverno": ["Sobretudo elegante + botas + bolsa vintage"]
        }
    },
    "casual": {
        "feliz": {
            "verão": ["Regata branca + shorts jeans + chinelo"],
            "inverno": ["Moletom divertido + calça comfy + tênis"]
        },
        "neutro": {
            "verão": ["Camiseta básica + bermuda + tênis branco"],
            "inverno": ["Gola alta + calça flare + bota"]
        },
        "triste": {
            "verão": ["Camiseta com estampa + jardineira + tênis"],
            "inverno": ["Blusão oversized + legging + meia divertida"]
        }
    }
}

def main(page: ft.Page):
    page.title = "👗 AIStyleMe - Seu Estilo Inteligente"
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.scroll = "auto"

    humor = ft.Dropdown(label="Como você está se sentindo hoje?", options=[
        ft.dropdown.Option("feliz"),
        ft.dropdown.Option("neutro"),
        ft.dropdown.Option("triste")
    ])

    estacao = ft.Dropdown(label="Qual estação do ano?", options=[
        ft.dropdown.Option("verão"),
        ft.dropdown.Option("inverno")
    ])

    ocasiao = ft.Dropdown(label="Qual ocasião?", options=[
        ft.dropdown.Option("trabalho"),
        ft.dropdown.Option("festa"),
        ft.dropdown.Option("casual")
    ])

    cor = ft.TextField(label="Qual sua cor preferida?", hint_text="Ex: Azul, Rosa, Preto")

    resultado = ft.Text("", size=16, weight="bold", color=ft.colors.PINK_800)

    def recomendar_look(e):
        if not humor.value or not estacao.value or not ocasiao.value or not cor.value:
            page.snack_bar = ft.SnackBar(ft.Text("Por favor, preencha todos os campos!"), bgcolor="red")
            page.snack_bar.open = True
            page.update()
            return

        try:
            sugestoes = recomendacoes[ocasiao.value][humor.value][estacao.value]
            sugestao = random.choice(sugestoes)
            resultado.value = f"👗 Recomendação de look: {sugestao}\n🌈 Toque de cor: {cor.value.title()} nos acessórios!"
        except:
            resultado.value = "Não foi possível gerar sugestão."

        page.update()

    page.add(
        ft.Text("✨ AIStyleMe - Consultor de Moda com Toque de IA", size=24, weight="bold"),
        humor,
        estacao,
        ocasiao,
        cor,
        ft.ElevatedButton("🎨 Ver Meu Estilo", on_click=recomendar_look),
        ft.Divider(),
        resultado
    )

ft.app(target=main)
