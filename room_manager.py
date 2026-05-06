# room_manager.py

class RoomManager:
    def __init__(self):
        # Database in memoria: Mappa tipo stanza -> {capacità totale, prenotate oggi}
        self.rooms = {
            "singola": {"capacity": 10, "booked": 0},
            "doppia": {"capacity": 5, "booked": 0},
            "suite": {"capacity": 2, "booked": 0}
        }

    def check_availability(self, room_type):
        """Restituisce il numero di stanze disponibili per un dato tipo."""
        if room_type not in self.rooms:
            return 0
        
        # Sottrae le prenotate dalla capacità totale
        available = self.rooms[room_type]["capacity"] - self.rooms[room_type]["booked"]
        # Assicuriamoci che la disponibilità non sia negativa a causa di prenotazioni errate passate
        return max(0, available) 

    def can_book(self, room_type, num_rooms):
        """Verifica se è possibile prenotare 'num_rooms' stanze."""
        # Aggiunto controllo per num_rooms <= 0
        if num_rooms <= 0:
            return False
        if room_type not in self.rooms:
            return False
            
        available = self.check_availability(room_type)

        if available >= num_rooms:
            return True
        return False

    def book_rooms(self, room_type, num_rooms):
        """Registra la prenotazione di un numero specifico di stanze."""
        # Verifica iniziale se il tipo di stanza esiste
        if room_type not in self.rooms:
            return False
            
        # Verifica se è possibile prenotare prima di modificare le stanze prenotate
        # La chiamata a can_book ora include la validazione per num_rooms
        if self.can_book(room_type, num_rooms):
            self.rooms[room_type]["booked"] += num_rooms
            return True
        return False # Se non è possibile prenotare, ritorna False senza modificare lo stato.

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
        # 1. Validare i parametri di input che non modificano lo stato
        # Aggiunto controllo per num_rooms <= 0
        if nights <= 0 or num_rooms <= 0:
            # Fallimento: numero di notti o stanze non valido.
            return None 
        
        # 2. Controlla e prenota le stanze (occupa la risorsa)
        # Questo passaggio è eseguito SOLO se le notti e le stanze sono valide.
        if not self.room_mgr.book_rooms(room_type, num_rooms):
            # Fallimento: stanze non disponibili o tipo stanza non valido.
            # La logica in RoomManager.book_rooms gestisce ora num_rooms <= 0 e capacità insufficiente.
            return None 

        # Se arriviamo qui, le stanze sono state prenotate con successo e le notti e stanze sono valide
        price_per_room = self.calculator.get_final_price(nights, is_low_season)
        total_price = price_per_room * num_rooms
        
        return total_price