def calcular_preco_total(ingredientes):
    precos = {
        'arroz': 5.0,
        'feijao': 4.0,
        'carne': 20.0,
        'frango': 15.0,
        'salada': 10.0,
        'batata': 3.0,
        'queijo': 8.0,
        'pao': 2.0,
    }
    
    total = 0.0
    ingredientes_invalidos = []

    for ingrediente in ingredientes:
        if ingrediente in precos:
            total += precos[ingrediente]
        else:
            ingredientes_invalidos.append(ingrediente)

    return total, ingredientes_invalidos

def main():
    print("Bem-vindo à Personalização de Refeições 🍽️")
    ingredientes = input("Digite os ingredientes desejados (separados por vírgula): ").split(',')
    ingredientes = [ingrediente.strip() for ingrediente in ingredientes]

    total, invalidos = calcular_preco_total(ingredientes)

    print(f"\nPreço total da refeição: R${total:.2f}")
    if invalidos:
        print("Ingredientes inválidos:", ', '.join(invalidos))

if __name__ == "__main__":
    main()