class Livro:
    def __init__(self, titulo, autor, genero):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero

class OrganizadorDeLivrosLidos:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, titulo, autor, genero):
        if not self._livro_existe(titulo):
            novo_livro = Livro(titulo, autor, genero)
            self.livros.append(novo_livro)
            print(f'Livro "{titulo}" adicionado com sucesso.')
        else:
            print(f'O livro "{titulo}" já está cadastrado.')

    def _livro_existe(self, titulo):
        return any(livro.titulo == titulo for livro in self.livros)

    def exibir_livros_por_genero(self):
        generos = {}
        for livro in self.livros:
            if livro.genero not in generos:
                generos[livro.genero] = []
            generos[livro.genero].append(livro)

        for genero, livros in generos.items():
            print(f'\nGênero: {genero}')
            for livro in livros:
                print(f' - {livro.titulo} por {livro.autor}')

# Exemplo de uso
if __name__ == "__main__":
    organizador = OrganizadorDeLivrosLidos()
    organizador.adicionar_livro("1984", "George Orwell", "Ficção")
    organizador.adicionar_livro("O Senhor dos Anéis", "J.R.R. Tolkien", "Fantasia")
    organizador.adicionar_livro("A Revolução dos Bichos", "George Orwell", "Ficção")
    organizador.exibir_livros_por_genero()