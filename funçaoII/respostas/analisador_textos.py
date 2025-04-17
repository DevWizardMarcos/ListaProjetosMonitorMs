def analisar_texto(texto):
    palavras = texto.split()
    total_palavras = len(palavras)
    palavras_unicas = set(palavras)
    palavras_repetidas = {palavra: palavras.count(palavra) for palavra in palavras_unicas}
    
    palavras_mais_repetidas = sorted(palavras_repetidas.items(), key=lambda item: item[1], reverse=True)
    
    return {
        "total_palavras": total_palavras,
        "palavras_mais_repetidas": palavras_mais_repetidas,
        "palavras_unicas": list(palavras_unicas)
    }

def main():
    texto = input("Cole seu texto aqui: ")
    resultado = analisar_texto(texto)
    
    print(f"Número total de palavras: {resultado['total_palavras']}")
    print("Palavras mais repetidas:")
    for palavra, contagem in resultado['palavras_mais_repetidas']:
        print(f"{palavra}: {contagem} vezes")
    print("Palavras únicas:", resultado['palavras_unicas'])

if __name__ == "__main__":
    main()