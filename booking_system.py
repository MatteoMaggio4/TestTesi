# booking_system.py
from room_manager import RoomManager
from discount_calculator import DiscountCalculator

class BookingSystem:
    def __init__(self):
        self.room_mgr = RoomManager()
        self.calculator = DiscountCalculator()

    def create_reservation(self, room_type, num_rooms, nights, is_low_season):
        """
        Crea una prenotazione completa.
        Ritorna il prezzo totale se successo, altrimenti None.
        """
        # 1. Validare i parametri di input prima di prenotare le stanze
        if nights <= 0:
            return None # Fallimento: numero di notti non valido

        # 2. Controlla e prenota le stanze (occupa la risorsa)
        if not self.room_mgr.book_rooms(room_type, num_rooms):
            return None # Fallimento: stanze non disponibili

        # Se arriviamo qui, le stanze sono state prenotate con successo e le notti sono valide
        price_per_room = self.calculator.get_final_price(nights, is_low_season)
        total_price = price_per_room * num_rooms
        
        return total_price

# Esempio di utilizzo
if __name__ == "__main__":
    system = BookingSystem()
    
    # Un utente malintenzionato o un errore di UI prova a prenotare per 0 notti
    print("Prezzo:", system.create_reservation("singola", 1, 0, False))
    
    # La stanza singola risulta occupata nonostante la prenotazione sia fallita!
    # Ora questa stampa dovrebbe riflettere correttamente lo stato del room_mgr
    print("Stanze singole prenotate:", system.room_mgr.rooms["singola"]["booked"])