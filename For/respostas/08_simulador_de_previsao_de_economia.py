# filepath: c:\Users\INFINITY SCHOOL\Desktop\Lista De Exercios Do Monitor Marrcos\For\08_simulador_de_previsao_de_economia.py

def savings_forecast(monthly_savings, years):
    total_savings = 0
    savings_over_time = []

    for year in range(1, years + 1):
        total_savings += monthly_savings * 12  # 12 months in a year
        savings_over_time.append((year, total_savings))

    return savings_over_time

def main():
    print("Simulador de Previsão de Economia")
    monthly_savings = float(input("Insira quanto você economiza por mês: "))
    years = int(input("Insira o número de anos para a previsão: "))

    forecast = savings_forecast(monthly_savings, years)

    print("\nPrevisão de Economia ao longo dos anos:")
    for year, total in forecast:
        print(f"Ano {year}: R${total:.2f}")

if __name__ == "__main__":
    main()