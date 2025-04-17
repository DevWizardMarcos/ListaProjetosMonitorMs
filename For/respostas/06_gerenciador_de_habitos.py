# filepath: c:\Users\INFINITY SCHOOL\Desktop\Lista De Exercios Do Monitor Marrcos\For\06_gerenciador_de_habitos.py

class HabitManager:
    def __init__(self):
        self.habits = {}

    def add_habit(self, habit_name):
        if habit_name not in self.habits:
            self.habits[habit_name] = []
            print(f"Hábito '{habit_name}' adicionado.")
        else:
            print(f"Hábito '{habit_name}' já existe.")

    def mark_habit(self, habit_name, day):
        if habit_name in self.habits:
            self.habits[habit_name].append(day)
            print(f"Hábito '{habit_name}' marcado para o dia {day}.")
        else:
            print(f"Hábito '{habit_name}' não encontrado.")

    def show_habits(self):
        if not self.habits:
            print("Nenhum hábito registrado.")
            return
        for habit, days in self.habits.items():
            print(f"Hábito: {habit}, Dias: {', '.join(days) if days else 'Nenhum dia marcado'}")

def main():
    manager = HabitManager()
    while True:
        print("\nGerenciador de Hábitos")
        print("1. Adicionar Hábito")
        print("2. Marcar Hábito")
        print("3. Mostrar Hábitos")
        print("4. Sair")
        choice = input("Escolha uma opção: ")

        if choice == '1':
            habit_name = input("Digite o nome do hábito: ")
            manager.add_habit(habit_name)
        elif choice == '2':
            habit_name = input("Digite o nome do hábito: ")
            day = input("Digite o dia (ex: '2023-10-01'): ")
            manager.mark_habit(habit_name, day)
        elif choice == '3':
            manager.show_habits()
        elif choice == '4':
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()