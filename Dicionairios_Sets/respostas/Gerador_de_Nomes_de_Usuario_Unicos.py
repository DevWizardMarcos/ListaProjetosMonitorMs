# Gerador_de_Nomes_de_Usuario_Unicos.py

import random
import string

class GeradorDeNomesDeUsuarioUnicos:
    def __init__(self):
        self.nomes_existentes = set()

    def gerar_nome_usuario(self, base_nome):
        nome_usuario = base_nome.lower().replace(" ", "_")
        sufixo = random.randint(1, 1000)
        nome_usuario_unico = f"{nome_usuario}_{sufixo}"

        while nome_usuario_unico in self.nomes_existentes:
            sufixo = random.randint(1, 1000)
            nome_usuario_unico = f"{nome_usuario}_{sufixo}"

        self.nomes_existentes.add(nome_usuario_unico)
        return nome_usuario_unico

    def verificar_nome_existente(self, nome_usuario):
        return nome_usuario in self.nomes_existentes

# Exemplo de uso
if __name__ == "__main__":
    gerador = GeradorDeNomesDeUsuarioUnicos()
    print(gerador.gerar_nome_usuario("João Silva"))
    print(gerador.gerar_nome_usuario("Maria Oliveira"))
    print(gerador.verificar_nome_existente("joão_silva_123"))  # Exemplo de verificação
