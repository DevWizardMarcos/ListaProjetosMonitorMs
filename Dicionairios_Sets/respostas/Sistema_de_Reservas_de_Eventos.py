class Reserva:
    def __init__(self, nome_evento, assentos_disponiveis):
        self.nome_evento = nome_evento
        self.assentos_disponiveis = assentos_disponiveis
        self.reservas = {}

    def reservar_assento(self, nome_cliente, quantidade):
        if quantidade > self.assentos_disponiveis:
            print("Não há assentos suficientes disponíveis.")
            return False
        if nome_cliente in self.reservas:
            print("Cliente já possui uma reserva.")
            return False
        
        self.reservas[nome_cliente] = quantidade
        self.assentos_disponiveis -= quantidade
        print(f"Reserva confirmada para {nome_cliente}: {quantidade} assentos.")
        return True

    def cancelar_reserva(self, nome_cliente):
        if nome_cliente not in self.reservas:
            print("Reserva não encontrada.")
            return False
        
        quantidade = self.reservas.pop(nome_cliente)
        self.assentos_disponiveis += quantidade
        print(f"Reserva cancelada para {nome_cliente}: {quantidade} assentos devolvidos.")
        return True

    def exibir_reservas(self):
        if not self.reservas:
            print("Nenhuma reserva feita.")
            return
        
        print("Reservas atuais:")
        for cliente, quantidade in self.reservas.items():
            print(f"{cliente}: {quantidade} assentos")