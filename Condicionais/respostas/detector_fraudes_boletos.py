# filepath: c:\Users\INFINITY SCHOOL\Desktop\Lista De Exercios Do Monitor Marrcos\Condicionais\detector_fraudes_boletos.py

def verificar_boleto(codigo_barras):
    # Verifica se o código de barras tem o tamanho correto
    if len(codigo_barras) != 44:
        return "Atenção: O código de barras deve ter 44 dígitos."

    # Aqui você pode adicionar mais validações se necessário

    return "Código de barras válido."

def main():
    codigo_barras = input("Insira o código de barras do boleto: ")
    resultado = verificar_boleto(codigo_barras)
    print(resultado)

if __name__ == "__main__":
    main()