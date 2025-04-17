# Calculadora de Economia para um Objetivo

# Solicita ao usuário o valor que deseja economizar e quanto pode guardar por mês
valor_objetivo = float(input("Digite o valor que deseja economizar: "))
valor_mensal = float(input("Digite quanto você pode guardar por mês: "))

# Inicializa o contador de meses e o total economizado
meses = 0
total_economizado = 0

# Loop para calcular o tempo necessário para atingir a meta
while total_economizado < valor_objetivo:
    meses += 1
    total_economizado += valor_mensal
    print(f"Mês {meses}: Você economizou R$ {total_economizado:.2f}")

# Exibe o resultado final
print(f"Você atingiu sua meta de R$ {valor_objetivo:.2f} em {meses} meses.")