# tradutor_emocoes.py

class MoodBot:
    def __init__(self):
        self.emotion_messages = {
            "feliz": "Estou tão feliz! 😊",
            "triste": "Sinto muito por você estar triste. 😢",
            "ansioso": "Entendo que você está ansioso. Respire fundo! 😌",
            "irritado": "Parece que você está irritado. Tente relaxar. 😤",
            "amoroso": "Que lindo! O amor está no ar! ❤️",
            "confuso": "É normal se sentir confuso às vezes. Vamos esclarecer isso. 🤔"
        }

    def translate_emotion_to_message(self, emotion):
        return self.emotion_messages.get(emotion.lower(), "Emoção não reconhecida. 😕")

def main():
    mood_bot = MoodBot()
    user_emotion = input("Digite sua emoção (feliz, triste, ansioso, irritado, amoroso, confuso): ")
    message = mood_bot.translate_emotion_to_message(user_emotion)
    print(message)

if __name__ == "__main__":
    main()