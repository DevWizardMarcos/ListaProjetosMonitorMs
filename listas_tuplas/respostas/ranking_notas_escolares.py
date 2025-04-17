def classificar_notas(notas):
    # Classifica as notas em ordem decrescente
    notas_classificadas = sorted(notas, reverse=True)
    
    # Obtém os três primeiros colocados
    primeiros_colocados = notas_classificadas[:3]
    
    return primeiros_colocados

def main():
    # Exemplo de uso
    notas = [7.5, 9.0, 8.5, 6.0, 10.0, 5.5]
    melhores_alunos = classificar_notas(notas)
    
    print("Os três primeiros colocados são:")
    for i, nota in enumerate(melhores_alunos, start=1):
        print(f"{i}º lugar: Nota {nota}")

if __name__ == "__main__":
    main()