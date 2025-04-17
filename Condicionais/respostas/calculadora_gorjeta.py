# filepath: c:\Users\INFINITY SCHOOL\Desktop\Lista De Exercios Do Monitor Marrcos\Condicionais\calculadora_gorjeta.py

def calcular_gorjeta():
    while True:
        try:
            valor_conta = float(input("Digite o valor da conta: R$ "))
            if valor_conta < 0:
                print("O valor da conta deve ser positivo. Tente novamente.")
                continue
            break
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")

    while True:
        nivel_atendimento = input("Digite o nível de atendimento (ruim, médio, ótimo): ").strip().lower()
        if nivel_atendimento == "ruim":
            porcentagem_gorjeta = 0.05
            break
        elif nivel_atendimento == "médio":
            porcentagem_gorjeta = 0.10
            break
        elif nivel_atendimento == "ótimo":
            porcentagem_gorjeta = 0.15
            break
        else:
            print("Nível de atendimento inválido. Tente novamente.")

    gorjeta = valor_conta * porcentagem_gorjeta
    total = valor_conta + gorjeta

    print(f"Gorjeta sugerida: R$ {gorjeta:.2f}")
    print(f"Valor total a ser pago: R$ {total:.2f}")

if __name__ == "__main__":
    calcular_gorjeta()