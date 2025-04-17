promocoes = {}

def adicionar_preco(produto, mercado, preco):
    if produto not in promocoes:
        promocoes[produto] = {}
    promocoes[produto][mercado] = preco
    print(f"🛍️ {produto} adicionado no {mercado} por R${preco:.2f}")

def melhor_preco(produto):
    if produto in promocoes:
        mercado = min(promocoes[produto], key=promocoes[produto].get)
        print(f"🏆 Melhor preço de {produto}: R${promocoes[produto][mercado]:.2f} no {mercado}")
    else:
        print("❌ Produto não encontrado.")

adicionar_preco("Arroz", "Mercado A", 10.50)
adicionar_preco("Arroz", "Mercado B", 9.80)
adicionar_preco("Feijão", "Mercado A", 8.00)
melhor_preco("Arroz")
melhor_preco("Feijão")
