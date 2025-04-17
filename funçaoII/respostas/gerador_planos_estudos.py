def gerador_planos_estudos(materias, tempo_por_dia, total_dias):
    cronograma = {}
    total_materias = len(materias)
    dias_por_materia = total_dias // total_materias

    for materia in materias:
        cronograma[materia] = dias_por_materia

    # Distribui os dias restantes, se houver
    dias_restantes = total_dias % total_materias
    for i in range(dias_restantes):
        cronograma[materias[i]] += 1

    return cronograma

# Exemplo de uso
if __name__ == "__main__":
    materias = ["Matemática", "Português", "História", "Ciências"]
    tempo_por_dia = 4  # horas
    total_dias = 10

    plano_estudos = gerador_planos_estudos(materias, tempo_por_dia, total_dias)
    for materia, dias in plano_estudos.items():
        print(f"{materia}: {dias} dias")