import random

def gerar_nome_projeto():
    adjetivos = ["Inovador", "Criativo", "Sustentável", "Inteligente", "Dinâmico", "Futurista", "Eficiente", "Colaborativo"]
    substantivos = ["Projeto", "Sistema", "Aplicativo", "Produto", "Serviço", "Modelo", "Estratégia", "Plataforma"]
    
    nome = f"{random.choice(adjetivos)} {random.choice(substantivos)}"
    return nome

def main():
    print("Gerador de Nomes Aleatórios para Projetos")
    while True:
        input("Pressione Enter para gerar um novo nome ou digite 'sair' para encerrar: ")
        print(gerar_nome_projeto())

if __name__ == "__main__":
    main()