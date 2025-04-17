# While/contador_de_habitos.py

def contador_de_habitos():
    habit = input("Defina um hábito: ")
    goal = int(input("Quantas vezes você quer completar esse hábito? "))
    count = 0

    while count < goal:
        completed = input(f"Você completou o hábito '{habit}'? (s/n): ")
        if completed.lower() == 's':
            count += 1
            print(f"Você completou o hábito {count} vez(es).")
        else:
            print("Continue tentando!")

    print(f"Parabéns! Você atingiu sua meta de {goal} vezes de '{habit}'.")

if __name__ == "__main__":
    contador_de_habitos()