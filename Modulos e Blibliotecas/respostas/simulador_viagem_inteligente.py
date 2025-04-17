destinos = {
    "Paris": {"moeda": "Euro", "custo_dia": 200},
    "Tóquio": {"moeda": "Iene", "custo_dia": 150},
    "Nova York": {"moeda": "Dólar", "custo_dia": 180}
}

def planejar_viagem(destino, dias):
    if destino in destinos:
        custo = destinos[destino]['custo_dia'] * dias
        print(f"Destino: {destino}")
        print(f"Custo Estimado: {custo} {destinos[destino]['moeda']}")
    else:
        print("Destino não encontrado!")

planejar_viagem("Paris", 5)
