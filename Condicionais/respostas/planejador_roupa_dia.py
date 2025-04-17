# filepath: c:\Users\INFINITY SCHOOL\Desktop\Lista De Exercios Do Monitor Marrcos\Condicionais\planejador_roupa_dia.py

def sugerir_roupa(temperatura):
    if temperatura < 15:
        return "Vista um casaco pesado!"
    elif 15 <= temperatura <= 25:
        return "Use uma blusa leve!"
    else:
        return "Vá de camiseta!"

def main():
    try:
        temperatura = float(input("Informe a temperatura atual em °C: "))
        roupa_sugerida = sugerir_roupa(temperatura)
        print(roupa_sugerida)
    except ValueError:
        print("Por favor, insira um número válido para a temperatura.")

if __name__ == "__main__":
    main()