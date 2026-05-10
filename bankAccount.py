class BankAccount:
    def __init__(self, initial_balance, daily_limit=1000.0):
        self.balance = initial_balance
        self.daily_limit = daily_limit
        # Rimosso self.withdrawn_today poiché la sua gestione corretta richiede logica temporale non permessa.
        # Il daily_limit sarà interpretato come un limite per singola transazione nel contesto di questa correzione.

    def withdraw(self, amount):
        """
        Preleva denaro dal conto.
        Verifica la disponibilità dei fondi e fa rispettare il limite
        giornaliero di prelievo associato al conto (interpretato come limite per transazione singola a causa dei vincoli).
        """
        if amount <= 0:
            raise ValueError("L'importo del prelievo deve essere maggiore di zero.")

        if amount > self.balance:
            raise ValueError("Fondi insufficienti sul conto.")

        # Il controllo viene effettuato direttamente sull'importo del prelievo rispetto al daily_limit.
        # Senza una logica di reset giornaliero, questo di fatto diventa un limite per transazione.
        if amount > self.daily_limit:
            raise ValueError("L'importo del prelievo supera il limite per transazione.")

        self.balance -= amount
        # self.withdrawn_today non viene più aggiornato poiché non può essere gestito correttamente.

        return self.balance