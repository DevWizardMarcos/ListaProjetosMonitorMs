def calcular_divisao_conta(valor_total, num_pessoas, percentual_gorjeta):
    gorjeta = valor_total * (percentual_gorjeta / 100)
    total_com_gorjeta = valor_total + gorjeta
    valor_por_pessoa = total_com_gorjeta / num_pessoas
    return valor_por_pessoa

def main():
    print("Calculadora de Divisão de Conta com Gorjeta")
    
    valor_total = float(input("Informe o valor total da conta: R$ "))
    num_pessoas = int(input("Informe o número de pessoas: "))
    percentual_gorjeta = float(input("Informe o percentual de gorjeta: "))

    valor_por_pessoa = calcular_divisao_conta(valor_total, num_pessoas, percentual_gorjeta)
    
    print(f"Cada pessoa deve pagar: R$ {valor_por_pessoa:.2f}")

if __name__ == "__main__":
    main()