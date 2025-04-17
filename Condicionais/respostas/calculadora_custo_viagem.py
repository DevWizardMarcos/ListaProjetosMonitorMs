# filepath: c:\Users\INFINITY SCHOOL\Desktop\Lista De Exercios Do Monitor Marrcos\Condicionais\calculadora_custo_viagem.py

def calcular_custo_viagem():
    try:
        distancia = float(input("Informe a distância da viagem em km: "))
        consumo = float(input("Informe o consumo do carro em km/L: "))
        preco_combustivel = float(input("Informe o preço médio do combustível por litro: "))

        if distancia < 0 or consumo <= 0 or preco_combustivel < 0:
            print("Por favor, insira valores positivos para distância, consumo e preço do combustível.")
            return

        litros_necessarios = distancia / consumo
        custo_total = litros_necessarios * preco_combustivel

        print(f"Custo total da viagem: R$ {custo_total:.2f}")

    except ValueError:
        print("Por favor, insira valores numéricos válidos.")

if __name__ == "__main__":
    calcular_custo_viagem()