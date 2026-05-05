# inventory.py

class Inventory:
    def __init__(self):
        # Database in memoria simulato
        self.products = {
            "laptop": {"stock": 5, "price": 1000.0},
            "mouse": {"stock": 10, "price": 25.0},
            "keyboard": {"stock": 0, "price": 45.0} # Esaurito
        }

    def is_in_stock(self, product_name):
        """Verifica se il prodotto è in magazzino."""
        if product_name in self.products and self.products[product_name]["stock"] > 0:
            return True
        return False

    def get_price(self, product_name):
        if product_name in self.products:
            return self.products[product_name]["price"]
        return 0.0

    def reduce_stock(self, product_name):
        """Riduce la giacenza di un prodotto di 1 unità."""
        if self.is_in_stock(product_name):
            self.products[product_name]["stock"] -= 1
            return True
        return False