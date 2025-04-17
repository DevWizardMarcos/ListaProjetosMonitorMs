import os
import shutil

class OrganizadorInteligente:
    def __init__(self, pasta_origem):
        self.pasta_origem = pasta_origem
        self.pasta_destino = os.path.join(pasta_origem, "Organizados")

        if not os.path.exists(self.pasta_destino):
            os.makedirs(self.pasta_destino)

    def organizar_arquivos(self):
        for arquivo in os.listdir(self.pasta_origem):
            if os.path.isfile(os.path.join(self.pasta_origem, arquivo)):
                self._mover_arquivo(arquivo)

    def _mover_arquivo(self, arquivo):
        extensao = arquivo.split('.')[-1]
        pasta_tipo = os.path.join(self.pasta_destino, extensao)

        if not os.path.exists(pasta_tipo):
            os.makedirs(pasta_tipo)

        shutil.move(os.path.join(self.pasta_origem, arquivo), os.path.join(pasta_tipo, arquivo))

if __name__ == "__main__":
    pasta_origem = input("Digite o caminho da pasta que deseja organizar: ")
    organizador = OrganizadorInteligente(pasta_origem)
    organizador.organizar_arquivos()
    print("Arquivos organizados com sucesso!")