def comparar_textos(texto1, texto2):
    # Divide os textos em frases
    frases_texto1 = set(texto1.split('. '))
    frases_texto2 = set(texto2.split('. '))
    
    # Encontra frases duplicadas
    frases_duplicadas = frases_texto1.intersection(frases_texto2)
    
    return frases_duplicadas

def main():
    texto1 = input("Digite o primeiro texto: ")
    texto2 = input("Digite o segundo texto: ")
    
    frases_duplicadas = comparar_textos(texto1, texto2)
    
    if frases_duplicadas:
        print("Frases idênticas encontradas:")
        for frase in frases_duplicadas:
            print(f"- {frase}")
    else:
        print("Nenhuma frase idêntica encontrada.")

if __name__ == "__main__":
    main()