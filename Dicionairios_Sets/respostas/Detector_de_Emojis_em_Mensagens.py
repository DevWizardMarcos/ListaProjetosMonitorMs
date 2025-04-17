# Detector_de_Emojis_em_Mensagens.py

def detectar_emojis(mensagem):
    emojis = {}
    for char in mensagem:
        if char in emojis:
            emojis[char] += 1
        elif char in emoji.UNICODE_EMOJI['en']:
            emojis[char] = 1
    return emojis

def exibir_resultados(emojis):
    if not emojis:
        print("Nenhum emoji encontrado.")
    else:
        for emoji, contagem in emojis.items():
            print(f"Emoji: {emoji}, Contagem: {contagem}")

def main():
    mensagem = input("Digite a mensagem: ")
    emojis_encontrados = detectar_emojis(mensagem)
    exibir_resultados(emojis_encontrados)

if __name__ == "__main__":
    main()