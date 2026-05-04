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
        
        # Verifica se l'utente può permettersi il prodotto
        if self.user_mgr.can_afford(username, price):
             # Tenta di dedurre il saldo. Se fallisce, significa che il saldo non è più sufficiente.
             if self.user_mgr.deduct_balance(username, price):
                 self.inventory.reduce_stock(product_name)
                 return "Successo: Ordine completato"
             else:
                 # Se deduct_balance fallisce dopo che can_afford era True,
                 # il motivo più probabile è che il saldo non è più sufficiente.
                 return "Fallito: Saldo insufficiente"
        else:
             # Saldo inizialmente insufficiente
             return "Fallito: Saldo insufficiente"

# Esempio di utilizzo (opzionale, ma aiuta a capire il flusso)
if __name__ == "__main__":
    processor = OrderProcessor()
    print(processor.process_order("mario80", "mouse"))