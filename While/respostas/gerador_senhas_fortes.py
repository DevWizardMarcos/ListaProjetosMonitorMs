import random
import string

def gerar_senha(tamanho=12, usar_letras=True, usar_numeros=True, usar_simbolos=True):
    caracteres = ''
    if usar_letras:
        caracteres += string.ascii_letters
    if usar_numeros:
        caracteres += string.digits
    if usar_simbolos:
        caracteres += string.punctuation

    if not caracteres:
        raise ValueError("Pelo menos uma categoria de caracteres deve ser selecionada.")

    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

def main():
    print("Gerador de Senhas Fortes")
    tamanho = int(input("Digite o tamanho da senha desejada: "))
    usar_letras = input("Incluir letras? (s/n): ").lower() == 's'
    usar_numeros = input("Incluir números? (s/n): ").lower() == 's'
    usar_simbolos = input("Incluir símbolos? (s/n): ").lower() == 's'

    senha = gerar_senha(tamanho, usar_letras, usar_numeros, usar_simbolos)
    print(f"Sua senha gerada é: {senha}")

if __name__ == "__main__":
    main()