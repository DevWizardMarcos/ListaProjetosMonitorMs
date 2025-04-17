def calcular_gastos_mensais(gastos):
    total_gastos = 0
    categorias = {}

    for gasto in gastos:
        categoria, valor = gasto
        total_gastos += valor
        if categoria in categorias:
            categorias[categoria] += valor
        else:
            categorias[categoria] = valor

    return total_gastos, categorias


def main():
    gastos = []
    while True:
        entrada = input("Insira seu gasto (categoria, valor) ou 'sair' para finalizar: ")
        if entrada.lower() == 'sair':
            break
        try:
            categoria, valor = entrada.split(',')
            gastos.append((categoria.strip(), float(valor.strip())))
        except ValueError:
            print("Entrada inválida. Use o formato 'categoria, valor'.")

    total, categorias = calcular_gastos_mensais(gastos)
    print(f"\nTotal de gastos: R${total:.2f}")
    print("Gastos por categoria:")
    for categoria, valor in categorias.items():
        print(f"{categoria}: R${valor:.2f}")


if __name__ == "__main__":
    main()