# filepath: c:\Users\INFINITY SCHOOL\Desktop\Lista De Exercios Do Monitor Marrcos\For\09_calculadora_de_gorjeta.py

def calcular_gorjeta(valor_conta, porcentagem_gorjeta):
    """
    Calcula o valor da gorjeta com base no valor da conta e na porcentagem escolhida.
    
    :param valor_conta: O valor total da conta.
    :param porcentagem_gorjeta: A porcentagem da gorjeta a ser calculada.
    :return: O valor da gorjeta.
    """
    return valor_conta * (porcentagem_gorjeta / 100)

def main():
    print("Calculadora de Gorjeta")
    
    try:
        valor_conta = float(input("Digite o valor da conta: R$ "))
        porcentagem_gorjeta = float(input("Digite a porcentagem da gorjeta (ex: 10 para 10%): "))
        
        gorjeta = calcular_gorjeta(valor_conta, porcentagem_gorjeta)
        total = valor_conta + gorjeta
        
        print(f"\nValor da gorjeta: R$ {gorjeta:.2f}")
        print(f"Valor total a pagar: R$ {total:.2f}")
        
    except ValueError:
        print("Por favor, insira um valor numérico válido.")

if __name__ == "__main__":
    main()