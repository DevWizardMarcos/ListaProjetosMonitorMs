import flet as ft
import random

# Lista de perguntas simuladas para entrevistas
perguntas_entrevista = [
    "Fale sobre você.",
    "Qual é o seu maior ponto forte?",
    "Qual foi seu maior desafio profissional?",
    "Onde você se vê em 5 anos?",
    "Por que devemos te contratar?",
    "Você prefere trabalhar sozinho ou em equipe?",
    "Fale sobre uma situação em que você resolveu um problema.",
]

def main(page: ft.Page):
    page.title = "JobHunter - Currículo e Entrevista"
    page.scroll = "auto"

    # Campos do currículo
    nome = ft.TextField(label="Nome completo", width=400)
    email = ft.TextField(label="Email", width=400)
    telefone = ft.TextField(label="Telefone", width=400)
    formacao = ft.TextField(label="Formação Acadêmica", multiline=True, width=400)
    experiencia = ft.TextField(label="Experiência Profissional", multiline=True, width=400)
    habilidades = ft.TextField(label="Habilidades", multiline=True, width=400)
    resultado_curriculo = ft.Text(value="", selectable=True)

    # Simulador de entrevista
    pergunta_simulada = ft.Text("", size=16, italic=True)

    def gerar_curriculo(e):
        resultado = f"""
📄 Currículo Gerado:

Nome: {nome.value}
Email: {email.value}
Telefone: {telefone.value}

🎓 Formação Acadêmica:
{formacao.value}

💼 Experiência Profissional:
{experiencia.value}

🛠️ Habilidades:
{habilidades.value}
"""
        resultado_curriculo.value = resultado
        page.update()

    def simular_pergunta(e):
        pergunta_simulada.value = f"🎤 {random.choice(perguntas_entrevista)}"
        page.update()

    page.add(
        ft.Text("📄 JobHunter - Montador de Currículo e Simulador de Entrevista", size=24, weight="bold"),
        nome, email, telefone,
        formacao, experiencia, habilidades,
        ft.ElevatedButton("Gerar Currículo", on_click=gerar_curriculo, bgcolor=ft.colors.GREEN),
        resultado_curriculo,
        ft.Divider(),
        ft.Text("🎯 Simulador de Entrevista", size=20, weight="bold"),
        ft.ElevatedButton("Mostrar Pergunta de Entrevista", on_click=simular_pergunta),
        pergunta_simulada
    )

ft.app(target=main)
