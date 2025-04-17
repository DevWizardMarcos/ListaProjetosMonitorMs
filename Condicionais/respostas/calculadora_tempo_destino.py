# filepath: c:\Users\INFINITY SCHOOL\Desktop\Lista De Exercios Do Monitor Marrcos\Condicionais\calculadora_tempo_destino.py

def calcular_tempo_destino():
    distancia = float(input("Informe a distância em km: "))
    meio_transporte = input("Informe o meio de transporte (carro, bicicleta, a pé): ").lower()

    if meio_transporte == "carro":
        tempo = distancia / 60  # média de 60 km/h
    elif meio_transporte == "bicicleta":
        tempo = distancia / 15  # média de 15 km/h
    elif meio_transporte == "a pé":
        tempo = distancia / 5  # média de 5 km/h
    else:
        print("Meio de transporte inválido.")
        return

    print(f"Tempo estimado de chegada: {tempo:.2f} horas.")

if __name__ == "__main__":
    calcular_tempo_destino()