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
        
        # Verifica se l'utente può permettersi il prodotto (saldo >= prezzo)
        if self.user_mgr.can_afford(username, price):
             # Qui è dove dovrebbe avvenire la deduzione del saldo
             if self.user_mgr.deduct_balance(username, price): # Aggiunto controllo per la deduzione effettiva
                 self.inventory.reduce_stock(product_name)
                 return "Successo: Ordine completato"
             else:
                 # Questo caso non dovrebbe verificarsi con la correzione in UserManager, 
                 # ma lo manteniamo per robustezza in caso di scenari di concorrenza non gestiti.
                 return "Fallito: Errore durante la deduzione del saldo"
        else:
             return "Fallito: Saldo insufficiente"

# Esempio di utilizzo (opzionale, ma aiuta a capire il flusso)
if __name__ == "__main__":
    processor = OrderProcessor()
    print(processor.process_order("mario80", "mouse"))