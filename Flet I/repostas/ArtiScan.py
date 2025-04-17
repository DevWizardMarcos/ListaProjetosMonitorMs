import flet as ft

# Simulando um "banco de dados" de produtos
produtos = {
    "001": {"nome": "Leite Integral", "preco": 4.99, "categoria": "Bebidas", "descricao": "Leite de vaca integral 1L"},
    "002": {"nome": "Arroz Branco", "preco": 23.50, "categoria": "Alimentos", "descricao": "Pacote de arroz branco 5kg"},
    "003": {"nome": "Sabonete", "preco": 2.50, "categoria": "Higiene", "descricao": "Sabonete com extrato de camomila"},
    "004": {"nome": "Detergente", "preco": 3.20, "categoria": "Limpeza", "descricao": "Detergente neutro 500ml"},
    "005": {"nome": "Biscoito Recheado", "preco": 2.99, "categoria": "Snacks", "descricao": "Biscoito de chocolate 120g"}
}

def main(page: ft.Page):
    page.title = "🛒 ArtiScan - Scanner de Produtos"
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.scroll = "auto"

    codigo_input = ft.TextField(label="Digite o código do produto", width=300)
    resultado = ft.Column()

    def buscar_produto(e):
        codigo = codigo_input.value.strip()
        resultado.controls.clear()

        if codigo in produtos:
            produto = produtos[codigo]
            resultado.controls.append(ft.Text(f"Produto: {produto['nome']}", size=20, weight="bold"))
            resultado.controls.append(ft.Text(f"Preço: R$ {produto['preco']:.2f}"))
            resultado.controls.append(ft.Text(f"Categoria: {produto['categoria']}"))
            resultado.controls.append(ft.Text(f"Descrição: {produto['descricao']}"))
        else:
            resultado.controls.append(ft.Text("❌ Produto não encontrado!", color=ft.colors.RED))

        page.update()

    page.add(
        ft.Text("🔎 ArtiScan - Simulador de Scanner de Produtos", size=26, weight="bold"),
        codigo_input,
        ft.ElevatedButton("Buscar Produto", on_click=buscar_produto),
        ft.Divider(),
        resultado
    )

ft.app(target=main)
