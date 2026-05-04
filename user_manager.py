# C:\Users\matte\Test-Tesi\user_manager.py
# user_manager.py

class UserManager:
    def __init__(self):
        # Database in memoria simulato
        self.users = {
            "mario80": {"balance": 150.0},
            "luigi99": {"balance": 50.0}
        }

    def can_afford(self, username, amount):
        """Verifica se l'utente ha abbastanza saldo."""
        if username not in self.users:
            return False
        
        user_balance = self.users[username]["balance"]
        
        # CORREZIONE: Usa >= per includere il caso di saldo esatto
        if user_balance >= amount: 
            return True
        return False

    def deduct_balance(self, username, amount):
        """Deduce l'importo dal saldo dell'utente."""
        # CORREZIONE: Aggiunto controllo per importi negativi
        if amount < 0:
            return False # Non si possono dedurre importi negativi (che equivarrebbero ad aggiungerli)

        if self.can_afford(username, amount):
            self.users[username]["balance"] -= amount
            return True
        return False