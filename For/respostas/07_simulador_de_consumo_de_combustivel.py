# Fuel Consumption Simulator

def calcular_consumo(distancia, consumo_medio):
    """Calcula o combustível utilizado com base na distância e no consumo médio."""
    return distancia / consumo_medio

def main():
    print("Simulador de Consumo de Combustível")
    
    try:
        distancia = float(input("Digite a distância percorrida (em km): "))
        consumo_medio = float(input("Digite o consumo médio do carro (em km/l): "))
        
        if consumo_medio <= 0:
            print("O consumo médio deve ser maior que zero.")
            return
        
        combustivel_usado = calcular_consumo(distancia, consumo_medio)
        print(f"Combustível utilizado: {combustivel_usado:.2f} litros")
    
    except ValueError:
        print("Por favor, insira valores numéricos válidos.")

if __name__ == "__main__":
    main()