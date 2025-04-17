def gerar_relatorio(dados_funcionarios):
    relatorio = "Relatório de Funcionários\n"
    relatorio += "=" * 30 + "\n"
    
    for funcionario in dados_funcionarios:
        nome, cargo, salario = funcionario
        relatorio += f"Nome: {nome}\nCargo: {cargo}\nSalário: R${salario:.2f}\n"
        relatorio += "-" * 30 + "\n"
    
    return relatorio

# Exemplo de uso
if __name__ == "__main__":
    funcionarios = [
        ("João Silva", "Desenvolvedor", 5000),
        ("Maria Oliveira", "Designer", 4500),
        ("Pedro Santos", "Gerente", 7000)
    ]
    
    relatorio = gerar_relatorio(funcionarios)
    print(relatorio)