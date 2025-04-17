import requests

def converter_moeda(valor, de_moeda, para_moeda):
    url = f"https://api.exchangerate-api.com/v4/latest/{de_moeda.upper()}"
    resposta = requests.get(url)
    
    if resposta.status_code != 200:
        return "Erro ao acessar a API."
    
    dados = resposta.json()
    taxas = dados.get("rates", {})

    if para_moeda.upper() not in taxas:
        return "Moeda de destino inválida."
    
    taxa = taxas[para_moeda.upper()]
    valor_convertido = valor * taxa
    return f"{valor} {de_moeda.upper()} = {valor_convertido:.2f} {para_moeda.upper()}"

# Exemplo de uso
print(converter_moeda(100, 'USD', 'EUR'))
