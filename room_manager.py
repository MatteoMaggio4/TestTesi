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
        # Controllo aggiuntivo per garantire che room_type esista prima di procedere
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
        if self.can_book(room_type, num_rooms):
            self.rooms[room_type]["booked"] += num_rooms
            return True
        return False