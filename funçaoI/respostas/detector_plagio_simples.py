# filepath: exercicios_monitor_marcos/detector_plagio_simples/main.py

def calcular_similaridade(texto1, texto2):
    palavras_texto1 = texto1.split()
    palavras_texto2 = texto2.split()
    
    palavras_comuns = set(palavras_texto1) & set(palavras_texto2)
    total_palavras = set(palavras_texto1) | set(palavras_texto2)
    
    if not total_palavras:
        return 0.0
    
    percentual_similaridade = len(palavras_comuns) / len(total_palavras) * 100
    return percentual_similaridade

def main():
    texto1 = input("Digite o primeiro texto: ")
    texto2 = input("Digite o segundo texto: ")
    
    similaridade = calcular_similaridade(texto1, texto2)
    print(f"O percentual de similaridade entre os textos é: {similaridade:.2f}%")

if __name__ == "__main__":
    main()