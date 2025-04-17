# While/temporizador_contagem_regressiva.py

import time

def temporizador_contagem_regressiva(segundos):
    while segundos:
        mins, secs = divmod(segundos, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end='\r')
        time.sleep(1)
        segundos -= 1
    print("Tempo esgotado!")

if __name__ == "__main__":
    try:
        tempo = int(input("Insira o tempo em segundos: "))
        temporizador_contagem_regressiva(tempo)
    except ValueError:
        print("Por favor, insira um número válido.")