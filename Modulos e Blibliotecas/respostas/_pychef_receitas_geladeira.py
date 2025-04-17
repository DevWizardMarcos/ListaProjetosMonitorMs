ingredientes_disponiveis = ["ovo", "leite", "farinha"]

receitas = {
    "Bolo Simples": ["ovo", "farinha", "leite"],
    "Omelete": ["ovo", "queijo"]
}

def encontrar_receitas(ingredientes):
    for nome, itens in receitas.items():
        if all(item in ingredientes for item in itens):
            print(f"Você pode fazer: {nome}")

encontrar_receitas(ingredientes_disponiveis)
