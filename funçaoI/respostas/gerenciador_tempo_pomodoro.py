# Gerenciador de Tempo e Pomodoro

import time
import winsound

class PomodoroTimer:
    def __init__(self, work_duration=25, break_duration=5):
        self.work_duration = work_duration * 60  # Convert to seconds
        self.break_duration = break_duration * 60  # Convert to seconds

    def start_work_session(self):
        print("Iniciando sessão de trabalho...")
        self.countdown(self.work_duration)
        print("Sessão de trabalho concluída!")

    def start_break(self):
        print("Iniciando pausa...")
        self.countdown(self.break_duration)
        print("Pausa concluída!")

    def countdown(self, duration):
        while duration:
            mins, secs = divmod(duration, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print(timer, end='\r')
            time.sleep(1)
            duration -= 1
        self.alert()

    def alert(self):
        print("Tempo esgotado!")
        # Sound alert (works on Windows)
        winsound.Beep(1000, 1000)  # Frequency, Duration in milliseconds

def main():
    pomodoro = PomodoroTimer()
    while True:
        pomodoro.start_work_session()
        pomodoro.start_break()

if __name__ == "__main__":
    main()