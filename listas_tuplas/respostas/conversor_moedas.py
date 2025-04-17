def conversor_moedas(valores, taxa_conversao):
    """
    Converte uma lista de valores para outra moeda usando uma taxa de conversão.

    :param valores: Lista de valores a serem convertidos.
    :param taxa_conversao: Taxa de conversão para a nova moeda.
    :return: Lista de valores convertidos.
    """
    valores_convertidos = [valor * taxa_conversao for valor in valores]
    return valores_convertidos

# Exemplo de uso
if __name__ == "__main__":
    valores_em_reais = [100, 200, 300]
    taxa_de_conversao = 0.18  # Exemplo: conversão de real para dólar
    valores_em_dolares = conversor_moedas(valores_em_reais, taxa_de_conversao)
    print("Valores em dólares:", valores_em_dolares)