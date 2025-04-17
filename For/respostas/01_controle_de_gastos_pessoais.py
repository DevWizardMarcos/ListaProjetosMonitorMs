# filepath: c:\Users\INFINITY SCHOOL\Desktop\Lista De Exercios Do Monitor Marrcos\For\01_controle_de_gastos_pessoais.py

def main():
    budget = float(input("Digite seu orçamento mensal: "))
    total_expenses = 0

    while True:
        expense = input("Digite um gasto diário (ou 'sair' para encerrar): ")
        if expense.lower() == 'sair':
            break
        try:
            total_expenses += float(expense)
            print(f"Gastos totais até agora: R${total_expenses:.2f}")
            if total_expenses > budget:
                print("Atenção: Você ultrapassou seu orçamento!")
        except ValueError:
            print("Por favor, insira um valor válido.")

    print(f"Gasto total no mês: R${total_expenses:.2f}")
    if total_expenses > budget:
        print("Você ultrapassou seu orçamento mensal.")
    else:
        print("Você está dentro do seu orçamento mensal.")

if __name__ == "__main__":
    main()