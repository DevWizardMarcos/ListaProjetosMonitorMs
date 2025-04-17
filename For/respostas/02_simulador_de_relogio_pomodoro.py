# filepath: c:\Users\INFINITY SCHOOL\Desktop\Lista De Exercios Do Monitor Marrcos\For\02_simulador_de_relogio_pomodoro.py

import time

def pomodoro_timer():
    work_duration = 25 * 60  # 25 minutes in seconds
    break_duration = 5 * 60   # 5 minutes in seconds
    cycles = 4

    for cycle in range(1, cycles + 1):
        print(f"Cycle {cycle}: Work for 25 minutes.")
        time.sleep(work_duration)  # Simulate work duration
        print("Time's up! Take a 5-minute break.")
        time.sleep(break_duration)  # Simulate break duration
        print("Break's over! Get back to work.")

if __name__ == "__main__":
    pomodoro_timer()