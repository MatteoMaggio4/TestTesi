class BankAccount:
    def __init__(self, initial_balance, daily_limit=1000.0):
        if initial_balance < 0:
            raise ValueError("Il saldo iniziale non può essere negativo.")
        self.balance = initial_balance
        if daily_limit < 0:
            raise ValueError("Il limite giornaliero non può essere negativo.")
        self.daily_limit = daily_limit
        self.withdrawn_today = 0.0
        # Assumiamo che esista una funzione per ottenere la data corrente,
        # e che venga chiamata all'inizio di una nuova sessione o giornata.
        # Per questo esempio, non implementiamo la logica di reset del giorno,
        # ma aggiungiamo un commento per indicare dove andrebbe inserita.
        self.last_withdrawal_day = None # Placeholder per la gestione del reset giornaliero

    def _reset_daily_withdrawal(self):
        # In un'applicazione reale, qui si controllerebbe la data corrente
        # e si resettarebbe withdrawn_today se il giorno è cambiato.
        # Esempio semplificato:
        # import datetime
        # today = datetime.date.today()
        # if self.last_withdrawal_day is None or today != self.last_withdrawal_day:
        #     self.withdrawn_today = 0.0
        #     self.last_withdrawal_day = today
        pass # Logica di reset giornaliero non implementata in questo snippet


    def withdraw(self, amount):
        """
        Preleva denaro dal conto.
        Verifica la disponibilità dei fondi e fa rispettare il limite
        giornaliero di prelievo associato al conto.
        """
        self._reset_daily_withdrawal() # Assicura che il contatore sia aggiornato per il giorno corrente

        if amount <= 0:
            raise ValueError("L'importo del prelievo deve essere maggiore di zero.")

        if amount > self.balance:
            raise ValueError("Fondi insufficienti sul conto.")

        # Controlla se l'importo del prelievo attuale, sommato a quanto già prelevato oggi, supera il limite.
        if self.withdrawn_today + amount > self.daily_limit:
            raise ValueError("Hai superato il limite di prelievo giornaliero.")

        self.balance -= amount
        self.withdrawn_today += amount
        # Potrebbe essere utile aggiornare self.last_withdrawal_day qui se _reset_daily_withdrawal
        # non è chiamato in ogni operazione e se si vuole tracciare il giorno dell'ultima transazione.
        # self.last_withdrawal_day = datetime.date.today()

        return self.balance

    def deposit(self, amount):
        """Deposita denaro sul conto."""
        if amount <= 0:
            raise ValueError("L'importo del deposito deve essere maggiore di zero.")
        self.balance += amount
        return self.balance