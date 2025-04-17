# filepath: c:\Users\INFINITY SCHOOL\Desktop\Lista De Exercios Do Monitor Marrcos\Condicionais\gerador_respostas_mensagens.py

def gerador_respostas_mensagens():
    print("Digite o tipo de mensagem recebida:")
    print("1. Cobrança de algo")
    print("2. Convite indesejado")
    print("3. Outro")
    
    tipo_mensagem = input("Escolha uma opção (1, 2 ou 3): ")

    if tipo_mensagem == "1":
        print("Resposta sugerida: 'Agradeço pela lembrança, mas estou resolvendo isso.'")
    elif tipo_mensagem == "2":
        print("Resposta sugerida: 'Agradeço o convite, mas não poderei participar.'")
    elif tipo_mensagem == "3":
        print("Resposta sugerida: 'Obrigado pela mensagem, vou pensar sobre isso.'")
    else:
        print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    gerador_respostas_mensagens()