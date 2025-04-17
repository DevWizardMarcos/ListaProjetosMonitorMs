# Roteiro de Viagem Inteligente

import json

class RoteiroViagemInteligente:
    def __init__(self):
        self.destinos = []
    
    def adicionar_destino(self, destino, atividades):
        self.destinos.append({
            'destino': destino,
            'atividades': atividades
        })
    
    def planejar_viagem(self, orcamento, interesses):
        # Lógica para sugerir destinos com base no orçamento e interesses
        sugestoes = []
        for destino in self.destinos:
            if self.verificar_orcamento(destino, orcamento) and self.verificar_interesses(destino, interesses):
                sugestoes.append(destino)
        return sugestoes
    
    def verificar_orcamento(self, destino, orcamento):
        # Implementar lógica para verificar se o destino está dentro do orçamento
        return True  # Placeholder
    
    def verificar_interesses(self, destino, interesses):
        # Implementar lógica para verificar se as atividades do destino correspondem aos interesses
        return True  # Placeholder
    
    def salvar_destinos(self, arquivo):
        with open(arquivo, 'w') as f:
            json.dump(self.destinos, f)
    
    def carregar_destinos(self, arquivo):
        with open(arquivo, 'r') as f:
            self.destinos = json.load(f)

if __name__ == "__main__":
    roteiro = RoteiroViagemInteligente()
    roteiro.adicionar_destino("Paris", ["Visitar a Torre Eiffel", "Museu do Louvre"])
    roteiro.adicionar_destino("Nova York", ["Central Park", "Estátua da Liberdade"])
    
    # Exemplo de planejamento de viagem
    orcamento = 2000
    interesses = ["cultura", "natureza"]
    sugestoes = roteiro.planejar_viagem(orcamento, interesses)
    
    print("Sugestões de viagem:", sugestoes)