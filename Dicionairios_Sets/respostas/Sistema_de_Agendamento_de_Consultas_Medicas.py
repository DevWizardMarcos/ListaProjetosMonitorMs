# Sistema de Agendamento de Consultas Médicas

class Consulta:
    def __init__(self, paciente, data_hora):
        self.paciente = paciente
        self.data_hora = data_hora

class SistemaAgendamento:
    def __init__(self):
        self.agendamentos = []

    def adicionar_consulta(self, paciente, data_hora):
        if not self.verificar_conflito(paciente, data_hora):
            nova_consulta = Consulta(paciente, data_hora)
            self.agendamentos.append(nova_consulta)
            return f"Consulta agendada para {paciente} em {data_hora}."
        else:
            return f"Conflito de agendamento: {paciente} já tem uma consulta nesse horário."

    def verificar_conflito(self, paciente, data_hora):
        for consulta in self.agendamentos:
            if consulta.paciente == paciente and consulta.data_hora == data_hora:
                return True
        return False

    def cancelar_consulta(self, paciente, data_hora):
        for consulta in self.agendamentos:
            if consulta.paciente == paciente and consulta.data_hora == data_hora:
                self.agendamentos.remove(consulta)
                return f"Consulta de {paciente} em {data_hora} cancelada."
        return f"Nenhuma consulta encontrada para {paciente} em {data_hora}."

    def listar_agendamentos(self):
        if not self.agendamentos:
            return "Nenhuma consulta agendada."
        return [f"{consulta.paciente} - {consulta.data_hora}" for consulta in self.agendamentos]