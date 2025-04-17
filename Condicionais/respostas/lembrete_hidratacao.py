# filepath: c:\Users\INFINITY SCHOOL\Desktop\Lista De Exercios Do Monitor Marrcos\Condicionais\lembrete_hidratacao.py

def lembrete_hidratacao():
    try:
        copos_consumidos = int(input("Quantos copos de água você bebeu hoje? "))
        
        if copos_consumidos < 8:
            print("Você deve beber mais água!")
        else:
            print("Ótimo! Você está bem hidratado.")
    
    except ValueError:
        print("Por favor, insira um número válido.")

if __name__ == "__main__":
    lembrete_hidratacao()