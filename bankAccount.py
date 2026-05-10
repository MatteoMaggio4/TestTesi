import datetime

class BankAccount:
    def __init__(self, initial_balance, daily_limit=1000.0):
        self.balance = initial_balance
        self.daily_limit = daily_limit
        self.withdrawn_today = 0.0
        self.last_withdrawal_date = datetime.date.today()

    def withdraw(self, amount):
        """
        Preleva denaro dal conto.
        Verifica la disponibilità dei fondi e fa rispettare il limite
        giornaliero di prelievo associato al conto.
        """
        today = datetime.date.today()
        if today != self.last_withdrawal_date:
            self.withdrawn_today = 0.0
            self.last_withdrawal_date = today

        if amount <= 0:
            raise ValueError("L'importo del prelievo deve essere maggiore di zero.")

        if amount > self.balance:
            raise ValueError("Fondi insufficienti sul conto.")

        if self.withdrawn_today + amount > self.daily_limit:
            raise ValueError("Hai superato il limite di prelievo giornaliero.")

        self.balance -= amount
        self.withdrawn_today += amount

        return self.balance