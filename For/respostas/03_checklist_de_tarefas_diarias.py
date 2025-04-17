# Checklist de Tarefas Diárias ✅

def main():
    tarefas = []

    while True:
        print("\nChecklist de Tarefas Diárias")
        print("1. Adicionar tarefa")
        print("2. Marcar tarefa como concluída")
        print("3. Listar tarefas")
        print("4. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            tarefa = input("Digite a tarefa a ser adicionada: ")
            tarefas.append({"tarefa": tarefa, "concluída": False})
            print(f"Tarefa '{tarefa}' adicionada.")
        
        elif escolha == '2':
            listar_tarefas(tarefas)
            indice = int(input("Digite o número da tarefa a ser marcada como concluída: ")) - 1
            if 0 <= indice < len(tarefas):
                tarefas[indice]["concluída"] = True
                print(f"Tarefa '{tarefas[indice]['tarefa']}' marcada como concluída.")
            else:
                print("Índice inválido.")
        
        elif escolha == '3':
            listar_tarefas(tarefas)
        
        elif escolha == '4':
            print("Saindo do checklist.")
            break
        
        else:
            print("Opção inválida. Tente novamente.")

def listar_tarefas(tarefas):
    if not tarefas:
        print("Nenhuma tarefa adicionada.")
        return
    print("\nTarefas:")
    for i, tarefa in enumerate(tarefas, start=1):
        status = "✅" if tarefa["concluída"] else "❌"
        print(f"{i}. {tarefa['tarefa']} - {status}")

if __name__ == "__main__":
    main()