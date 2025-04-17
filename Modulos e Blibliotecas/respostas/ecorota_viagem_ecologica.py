transportes = {
    "Carro": 120,
    "Ônibus": 80,
    "Avião": 300,
    "Bicicleta": 0
}

def comparar_emissao(distancia):
    for transporte, co2 in transportes.items():
        emissao_total = (co2/1000) * distancia
        print(f"{transporte}: {emissao_total:.2f} kg CO2")

comparar_emissao(500)  # Distância em quilômetros
