consultas = {}

def agendar_consulta(paciente, data, horario):
    if data in consultas and paciente in consultas[data]:
        print(f"⚠️ {paciente} já tem uma consulta marcada nesse dia!")
    else:
        consultas.setdefault(data, {}).update({paciente: horario})
        print(f"✅ Consulta marcada para {paciente} em {data} às {horario}!")

def cancelar_consulta(paciente, data):
    if data in consultas and paciente in consultas[data]:
        del consultas[data][paciente]
        print(f"🗑️ Consulta de {paciente} cancelada em {data}!")
    else:
        print("❌ Nenhuma consulta encontrada para esse paciente nesta data.")

agendar_consulta("João", "2025-04-10", "14:00")
agendar_consulta("Maria", "2025-04-10", "15:00")
agendar_consulta("João", "2025-04-10", "16:00")  # Tenta marcar de novo
cancelar_consulta("João", "2025-04-10")
print(consultas)


