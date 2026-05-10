class InventoryReserve:
    def __init__(self, available_units, max_reservation=20):
        self.available_units = available_units
        self.max_reservation = max_reservation
        self.reserved_today = 0

    def reserve(self, units):
        """
        Riserva un numero di unita di magazzino per il flusso ordine.
        Il limite massimo di prenotazione giornaliera deve considerare
        anche le prenotazioni gia effettuate nella giornata.
        """
        if units <= 0:
            raise ValueError("Le unita da riservare devono essere maggiori di zero.")

        if units > self.available_units:
            raise ValueError("Unita disponibili insufficienti.")

        # Correzione: Verifica che l'aggiunta delle nuove unità non superi il limite giornaliero totale
        if self.reserved_today + units > self.max_reservation:
            raise ValueError("Limite giornaliero di prenotazione superato.")

        self.available_units -= units
        self.reserved_today += units
        return self.available_units