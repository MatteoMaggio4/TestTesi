# discount_calculator.py

class DiscountCalculator:
    def __init__(self):
        self.base_price_per_night = 100.0

    def calculate_discount(self, nights, is_low_season):
        """
        Calcola lo sconto percentuale da applicare.
        Regole:
        - Bassa stagione: 10% di sconto.
        - Soggiorni lunghi (>= 7 notti): 15% di sconto.
        - Gli sconti NON sono cumulabili (si applica il maggiore).
        """
        low_season_discount = 0.0
        long_stay_discount = 0.0

        if is_low_season:
            low_season_discount = 10.0
            
        if nights >= 7:
            long_stay_discount = 15.0 

        return max(low_season_discount, long_stay_discount) # Applica lo sconto maggiore

    def get_final_price(self, nights, is_low_season):
        """Calcola il prezzo finale totale."""
        total_base = self.base_price_per_night * nights
        discount_pct = self.calculate_discount(nights, is_low_season)
        
        discount_amount = total_base * (discount_pct / 100.0)
        return total_base - discount_amount

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
        return available

    def can_book(self, room_type, num_rooms):
        """Verifica se è possibile prenotare 'num_rooms' stanze."""
        available = self.check_availability(room_type)

        if available >= num_rooms:
            return True
        return False

    def book_rooms(self, room_type, num_rooms):
        """Registra la prenotazione di un numero specifico di stanze."""
        # Aggiunto controllo prima di modificare le stanze prenotate
        if room_type not in self.rooms:
            return False
            
        if self.can_book(room_type, num_rooms):
            self.rooms[room_type]["booked"] += num_rooms
            return True
        return False