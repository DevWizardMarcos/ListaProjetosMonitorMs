# Importando bibliotecas necessárias
import speech_recognition as sr
import pyttsx3
import os

# Inicializando o reconhecedor de voz e o sintetizador de fala
recognizer = sr.Recognizer()
synthesizer = pyttsx3.init()

# Função para falar um texto
def falar(texto):
    synthesizer.say(texto)
    synthesizer.runAndWait()

# Função para adicionar um recado
def adicionar_recado(recado):
    with open("recados.txt", "a") as arquivo:
        arquivo.write(recado + "\n")
    falar("Recado adicionado com sucesso.")

# Função para ler os recados
def ler_recados():
    if os.path.exists("recados.txt"):
        with open("recados.txt", "r") as arquivo:
            recados = arquivo.readlines()
            if recados:
                for recado in recados:
                    falar(recado.strip())
            else:
                falar("Não há recados para ler.")
    else:
        falar("Não há recados para ler.")

# Função principal
def main():
    falar("Bem-vindo ao Assistente Virtual de Recados por Voz.")
    while True:
        falar("Você pode dizer 'adicionar recado' ou 'ler recados'.")
        with sr.Microphone() as source:
            audio = recognizer.listen(source)
            try:
                comando = recognizer.recognize_google(audio, language='pt-BR')
                if "adicionar recado" in comando:
                    falar("Por favor, diga o recado.")
                    audio = recognizer.listen(source)
                    recado = recognizer.recognize_google(audio, language='pt-BR')
                    adicionar_recado(recado)
                elif "ler recados" in comando:
                    ler_recados()
                elif "sair" in comando:
                    falar("Saindo do assistente.")
                    break
                else:
                    falar("Comando não reconhecido. Tente novamente.")
            except sr.UnknownValueError:
                falar("Desculpe, não consegui entender o que você disse.")
            except sr.RequestError:
                falar("Desculpe, houve um erro ao conectar ao serviço de reconhecimento de voz.")

if __name__ == "__main__":
    main()