# While/simulador_academia.py

def simulador_academia():
    exercicios = {
        "Flexões": 10,
        "Agachamentos": 15,
        "Abdominais": 20,
        "Corrida (em minutos)": 30
    }

    print("Bem-vindo ao Simulador de Academia!")
    print("Você precisará realizar as seguintes repetições:")

    for exercicio, repeticoes in exercicios.items():
        print(f"{exercicio}: {repeticoes} repetições")

    print("\nBom treino!")

if __name__ == "__main__":
    simulador_academia()