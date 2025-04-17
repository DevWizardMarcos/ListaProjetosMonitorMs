def gerar_desculpa():
    import random

    desculpas = [
        "Desculpe pelo atraso, meu carro quebrou no caminho.",
        "Peço desculpas, fiquei preso em um engarrafamento inesperado.",
        "Sinto muito, perdi a noção do tempo enquanto trabalhava em um projeto.",
        "Desculpe, tive um imprevisto familiar que me atrasou.",
        "Peço desculpas, meu despertador não tocou e eu acabei dormindo demais.",
        "Sinto muito, precisei ajudar um amigo em uma emergência.",
        "Desculpe, o transporte público estava atrasado hoje.",
        "Peço desculpas, tive que resolver um problema urgente no trabalho."
    ]

    return random.choice(desculpas)

if __name__ == "__main__":
    print(gerar_desculpa())