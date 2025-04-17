# chatbot_simulacao_conversa/main.py

class Chatbot:
    def __init__(self):
        self.responses = {
            "olá": "Olá! Como posso ajudar você hoje?",
            "como você está?": "Estou apenas um programa, mas obrigado por perguntar!",
            "qual é o seu nome?": "Eu sou um chatbot criado para simular conversas.",
            "adeus": "Até logo! Tenha um ótimo dia!",
        }

    def get_response(self, user_input):
        user_input = user_input.lower()
        return self.responses.get(user_input, "Desculpe, não entendi o que você disse.")

def main():
    chatbot = Chatbot()
    print("Bem-vindo ao Chatbot! Digite 'adeus' para sair.")
    
    while True:
        user_input = input("Você: ")
        if user_input.lower() == "adeus":
            print(chatbot.get_response(user_input))
            break
        response = chatbot.get_response(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    main()