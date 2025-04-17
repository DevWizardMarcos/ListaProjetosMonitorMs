def recomendar_filmes(humor, tempo):
    filmes = {
        "feliz": ["A Vida é Bela", "Intocáveis", "O Fabuloso Destino de Amélie Poulain"],
        "triste": ["A Espera de um Milagre", "A Lista de Schindler", "O Pianista"],
        "ansioso": ["Cisne Negro", "O Silêncio dos Inocentes", "Garota Exemplar"],
        "relaxado": ["A Praia", "Comer, Rezar, Amar", "O Lado Bom da Vida"],
        "chuvoso": ["O Fabuloso Destino de Amélie Poulain", "A Teoria de Tudo", "O Grande Hotel Budapeste"],
        "ensolarado": ["O Rei Leão", "Os Incríveis", "A Era do Gelo"]
    }

    if humor in filmes:
        recomendacoes = filmes[humor]
    else:
        recomendacoes = ["Desculpe, não temos recomendações para esse humor."]

    if tempo == "curto":
        recomendacoes = recomendacoes[:2]  # Sugere apenas 2 filmes para tempo curto

    return recomendacoes


# Exemplo de uso
if __name__ == "__main__":
    humor_usuario = input("Qual é o seu humor? (feliz, triste, ansioso, relaxado): ").strip().lower()
    tempo_usuario = input("Você tem tempo curto ou longo para assistir a um filme? (curto/longo): ").strip().lower()

    filmes_recomendados = recomendar_filmes(humor_usuario, tempo_usuario)
    print("Filmes recomendados:", filmes_recomendados)