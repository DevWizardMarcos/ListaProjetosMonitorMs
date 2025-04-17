# Contador de Palavras em um Texto

def contar_palavras(texto):
    # Divide o texto em palavras usando espaços como delimitadores
    palavras = texto.split()
    return len(palavras)

def main():
    texto_usuario = input("Insira um texto: ")
    total_palavras = contar_palavras(texto_usuario)
    print(f"O total de palavras no texto é: {total_palavras}")

if __name__ == "__main__":
    main()