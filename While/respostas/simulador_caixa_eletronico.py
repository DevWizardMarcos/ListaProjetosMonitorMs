# While/simulador_caixa_eletronico.py

def simulador_caixa_eletronico():
    # Dicionário com a quantidade de cédulas disponíveis
    cedulas = {
        100: 10,
        50: 10,
        20: 10,
        10: 10,
        5: 10,
        1: 10
    }

    # Solicita o valor do saque
    valor_saque = int(input("Digite o valor que deseja sacar: "))

    # Verifica se o valor é válido
    if valor_saque <= 0:
        print("Valor inválido. O valor deve ser maior que zero.")
        return

    # Armazena a quantidade de cédulas a serem entregues
    cedulas_entregues = {}

    # Calcula a quantidade de cédulas necessárias
    for nota in sorted(cedulas.keys(), reverse=True):
        while valor_saque >= nota and cedulas[nota] > 0:
            valor_saque -= nota
            cedulas[nota] -= 1
            if nota in cedulas_entregues:
                cedulas_entregues[nota] += 1
            else:
                cedulas_entregues[nota] = 1

    # Exibe o resultado
    if valor_saque == 0:
        print("Cédulas entregues:")
        for nota, quantidade in cedulas_entregues.items():
            print(f"{quantidade} cédula(s) de R${nota}")
    else:
        print("Desculpe, não há cédulas suficientes para o valor solicitado.")

# Chama a função para executar o simulador
simulador_caixa_eletronico()