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
        
        # Usa >= per includere il caso di saldo esatto
        return user_balance >= amount

    def deduct_balance(self, username, amount):
        """Deduce l'importo dal saldo dell'utente.
        Ritorna True se la deduzione è avvenuta con successo, False altrimenti.
        """
        if amount < 0:
            return False # Non si possono dedurre importi negativi

        if username not in self.users:
            return False # Utente non esistente

        # CONTROLLO CRITICO: Verifica il saldo disponibile PRIMA della deduzione effettiva
        # Questo è più robusto di un controllo separato 'can_afford' che potrebbe essere obsoleto
        # in un ambiente concorrente.
        if self.users[username]["balance"] < amount:
            return False # Saldo insufficiente

        self.users[username]["balance"] -= amount
        return True