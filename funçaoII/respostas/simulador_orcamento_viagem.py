def simulador_orcamento_viagem():
    print("Bem-vindo ao Simulador de Orçamento de Viagem!")
    
    # Coleta de informações do usuário
    pais_destino = input("Informe o país de destino: ")
    dias_viagem = int(input("Informe o número de dias de viagem: "))
    orcamento_total = float(input("Informe o orçamento total: "))
    moeda_original = input("Informe a moeda original: ")
    
    # Simulação de orçamento
    custo_diario = orcamento_total / dias_viagem
    print(f"\nPara uma viagem de {dias_viagem} dias para {pais_destino},")
    print(f"Você deve gastar aproximadamente {custo_diario:.2f} {moeda_original} por dia.")
    
    # Conversão de moeda (exemplo simples, sem taxas reais)
    taxa_conversao = 1.0  # Aqui você pode implementar uma lógica de conversão real
    orcamento_convertido = orcamento_total * taxa_conversao
    print(f"Seu orçamento total em {moeda_original} é {orcamento_total:.2f}.")
    print(f"Em moeda local, isso seria aproximadamente {orcamento_convertido:.2f}.")

if __name__ == "__main__":
    simulador_orcamento_viagem()