class Contato:
    def __init__(self, nome, telefone, email):
        self.nome = nome
        self.telefone = telefone
        self.email = email

class GerenciadorDeContatos:
    def __init__(self):
        self.contatos = {}

    def adicionar_contato(self, nome, telefone, email):
        if nome not in self.contatos:
            self.contatos[nome] = Contato(nome, telefone, email)
            print(f"Contato '{nome}' adicionado com sucesso.")
        else:
            print(f"Contato '{nome}' já existe.")

    def buscar_contato(self, nome):
        contato = self.contatos.get(nome)
        if contato:
            return f"Nome: {contato.nome}, Telefone: {contato.telefone}, Email: {contato.email}"
        else:
            return f"Contato '{nome}' não encontrado."

    def remover_contato(self, nome):
        if nome in self.contatos:
            del self.contatos[nome]
            print(f"Contato '{nome}' removido com sucesso.")
        else:
            print(f"Contato '{nome}' não encontrado.")

    def listar_contatos(self):
        if self.contatos:
            return [f"Nome: {contato.nome}, Telefone: {contato.telefone}, Email: {contato.email}" for contato in self.contatos.values()]
        else:
            return "Nenhum contato cadastrado."

# Exemplo de uso
if __name__ == "__main__":
    gerenciador = GerenciadorDeContatos()
    gerenciador.adicionar_contato("João", "1234-5678", "joao@email.com")
    print(gerenciador.buscar_contato("João"))
    gerenciador.remover_contato("João")
    print(gerenciador.listar_contatos())