# filepath: c:\Users\INFINITY SCHOOL\Desktop\Lista De Exercios Do Monitor Marrcos\Condicionais\detector_promocoes.py

def calcular_promocao(preco_original, preco_desconto):
    desconto = ((preco_original - preco_desconto) / preco_original) * 100
    
    if desconto > 50:
        return "Promoção incrível!"
    elif 20 <= desconto <= 50:
        return "Boa promoção!"
    else:
        return "Desconto pequeno, talvez não valha a pena."

def main():
    try:
        preco_original = float(input("Digite o preço original do produto: "))
        preco_desconto = float(input("Digite o preço com desconto: "))
        
        if preco_original <= 0 or preco_desconto < 0:
            print("Os preços devem ser positivos.")
            return
        
        resultado = calcular_promocao(preco_original, preco_desconto)
        print(resultado)
    except ValueError:
        print("Por favor, insira valores numéricos válidos.")

if __name__ == "__main__":
    main()