import random

def escolher_palavra():
    palavras = ["python", "programacao", "desenvolvimento", "computador", "algoritmo"]
    return random.choice(palavras)

def jogo_da_forca():
    palavra_secreta = escolher_palavra()
    letras_adivinhadas = []
    tentativas = 6
    venceu = False

    print("Bem-vindo ao Jogo da Forca!")
    
    while not venceu and tentativas > 0:
        print("\nPalavra:", " ".join([letra if letra in letras_adivinhadas else "_" for letra in palavra_secreta]))
        print(f"Tentativas restantes: {tentativas}")
        letra = input("Adivinhe uma letra: ").lower()

        if letra in letras_adivinhadas:
            print("Você já adivinhou essa letra. Tente outra.")
        elif letra in palavra_secreta:
            letras_adivinhadas.append(letra)
            print("Boa! Você acertou uma letra.")
        else:
            letras_adivinhadas.append(letra)
            tentativas -= 1
            print("Ops! Essa letra não está na palavra.")

        if all(letra in letras_adivinhadas for letra in palavra_secreta):
            venceu = True

    if venceu:
        print(f"Parabéns! Você adivinhou a palavra: {palavra_secreta}")
    else:
        print(f"Você perdeu! A palavra era: {palavra_secreta}")

if __name__ == "__main__":
    jogo_da_forca()