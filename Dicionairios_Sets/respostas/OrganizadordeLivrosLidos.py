livros = {}

def adicionar_livro(titulo, genero):
    if genero in livros:
        if titulo in livros[genero]:
            print("⚠️ Esse livro já está na lista!")
            return
        livros[genero].add(titulo)
    else:
        livros[genero] = {titulo}
    print(f"📖 '{titulo}' adicionado na categoria {genero}!")

def listar_livros():
    for genero, titulos in livros.items():
        print(f"\n📚 {genero}:")
        for titulo in titulos:
            print(f"- {titulo}")

adicionar_livro("1984", "Ficção Científica")
adicionar_livro("A Revolução dos Bichos", "Ficção Científica")
adicionar_livro("1984", "Ficção Científica")  # Repetido
listar_livros()
