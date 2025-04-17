# Rastreador de Promoções em Supermercados

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Supermarket:
    def __init__(self, name):
        self.name = name
        self.products = {}

    def add_product(self, product):
        self.products[product.name] = product.price

    def get_price(self, product_name):
        return self.products.get(product_name, None)

class PriceTracker:
    def __init__(self):
        self.supermarkets = {}

    def add_supermarket(self, supermarket):
        self.supermarkets[supermarket.name] = supermarket

    def add_product_to_supermarket(self, supermarket_name, product):
        if supermarket_name in self.supermarkets:
            self.supermarkets[supermarket_name].add_product(product)

    def find_best_price(self, product_name):
        best_price = float('inf')
        best_supermarket = None

        for supermarket in self.supermarkets.values():
            price = supermarket.get_price(product_name)
            if price is not None and price < best_price:
                best_price = price
                best_supermarket = supermarket.name

        return best_supermarket, best_price if best_supermarket else (None, None)

# Example usage
if __name__ == "__main__":
    tracker = PriceTracker()

    # Adding supermarkets
    market1 = Supermarket("Supermercado A")
    market2 = Supermarket("Supermercado B")

    tracker.add_supermarket(market1)
    tracker.add_supermarket(market2)

    # Adding products
    tracker.add_product_to_supermarket("Supermercado A", Product("Arroz", 5.50))
    tracker.add_product_to_supermarket("Supermercado A", Product("Feijão", 4.00))
    tracker.add_product_to_supermarket("Supermercado B", Product("Arroz", 5.00))
    tracker.add_product_to_supermarket("Supermercado B", Product("Feijão", 4.50))

    # Finding the best price
    best_market, best_price = tracker.find_best_price("Arroz")
    print(f"O melhor preço para 'Arroz' é {best_price} no {best_market}.")