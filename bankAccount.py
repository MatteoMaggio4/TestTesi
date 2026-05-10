class BankAccount:
    def __init__(self, initial_balance, daily_limit=1000.0):
        self.balance = initial_balance
        self.daily_limit = daily_limit
        self.withdrawn_today = 0.0
        # È necessario anche un meccanismo per resettare withdrawn_today,
        # ma questo va oltre il metodo withdraw e implica una gestione
        # della giornata che non è presente in questo snippet.
        # Per la correzione del solo metodo withdraw, ci focalizziamo
        # sull'uso corretto del limite giornaliero.

    def withdraw(self, amount):
        """
        Preleva denaro dal conto.
        Verifica la disponibilità dei fondi e fa rispettare il limite
        giornaliero di prelievo associato al conto.
        """
        if amount <= 0:
            raise ValueError("L'importo del prelievo deve essere maggiore di zero.")

        if amount > self.balance:
            raise ValueError("Fondi insufficienti sul conto.")

        # Correzione: verificare se l'importo del prelievo sommato a quello già prelevato supera il limite giornaliero.
        if self.withdrawn_today + amount > self.daily_limit:
            raise ValueError("Hai superato il limite di prelievo giornaliero.")

        self.balance -= amount
        self.withdrawn_today += amount

        return self.balance