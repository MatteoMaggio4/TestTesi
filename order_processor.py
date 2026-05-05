# order_processor.py
from user_manager import UserManager
from inventory import Inventory

class OrderProcessor:
    def __init__(self):
        self.user_mgr = UserManager()
        self.inventory = Inventory()

    def process_order(self, username, product_name):
        """Elabora un ordine completo."""
        
        if not self.inventory.is_in_stock(product_name):
            return "Fallito: Prodotto non disponibile"
            
        price = self.inventory.get_price(product_name)
        
      
        if self.user_mgr.can_afford(username, price):
             self.inventory.reduce_stock(product_name)
             return "Successo: Ordine completato"
        else:
             return "Fallito: Saldo insufficiente"

# Esempio di utilizzo
if __name__ == "__main__":
    processor = OrderProcessor()
    print(processor.process_order("mario80", "mouse"))