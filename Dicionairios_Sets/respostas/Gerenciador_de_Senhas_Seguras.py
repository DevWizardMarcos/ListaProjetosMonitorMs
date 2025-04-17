class PasswordManager:
    def __init__(self):
        self.passwords = {}

    def add_password(self, service, password):
        """Adiciona uma senha para um serviço."""
        if service in self.passwords:
            print(f"A senha para '{service}' já está cadastrada.")
        else:
            self.passwords[service] = password
            print(f"Senha para '{service}' adicionada com sucesso.")

    def get_password(self, service):
        """Recupera a senha de um serviço."""
        return self.passwords.get(service, "Serviço não encontrado.")

    def remove_password(self, service):
        """Remove a senha de um serviço."""
        if service in self.passwords:
            del self.passwords[service]
            print(f"Senha para '{service}' removida com sucesso.")
        else:
            print(f"Serviço '{service}' não encontrado.")

    def list_services(self):
        """Lista todos os serviços cadastrados."""
        return list(self.passwords.keys())

# Exemplo de uso
if __name__ == "__main__":
    manager = PasswordManager()
    manager.add_password("Email", "senha123")
    print(manager.get_password("Email"))
    manager.remove_password("Email")
    print(manager.list_services())