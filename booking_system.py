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
        if nights <= 0:
            # Fallimento: numero di notti non valido per il calcolo del prezzo e soggiorno.
            # Manteniamo questo fallimento perché un soggiorno di 0 notti non ha senso per il prezzo.
            return None 
        
        # 2. Controlla e prenota le stanze (occupa la risorsa)
        # Questo passaggio è eseguito SOLO se le notti sono valide.
        if not self.room_mgr.book_rooms(room_type, num_rooms):
            # Fallimento: stanze non disponibili.
            return None 

        # Se arriviamo qui, le stanze sono state prenotate con successo e le notti sono valide
        price_per_room = self.calculator.get_final_price(nights, is_low_season)
        total_price = price_per_room * num_rooms
        
        return total_price

# Esempio di utilizzo
if __name__ == "__main__":
    system = BookingSystem()
 
    # Esempio 1: Numero di notti non valido
    print(f"Tentativo prenotazione con 0 notti:")
    result_zero_nights = system.create_reservation("singola", 1, 0, False)
    print(f"Risultato: {result_zero_nights}")
    # L'accesso diretto a room_mgr.rooms qui è solo per dimostrazione dell'effetto dello stato.
    # In un caso reale, se create_reservation ritorna None, potremmo non voler ispezionare lo stato interno.
    print(f"Stanze singole prenotate dopo tentativo fallito (0 notti): {system.room_mgr.rooms.get('singola', {}).get('booked', 'Tipo stanza non trovato')}")
    print("-" * 20)

    # Reset delle stanze per il prossimo test (se necessario, in questo caso non è necessario perché non è stato prenotato nulla)
    # system = BookingSystem() # Opzionale per isolare i test se necessario, ma qui il booking fallisce prima.

    # Esempio 2: Stanze non disponibili
    print(f"Tentativo prenotazione di stanze non disponibili:")
    # Riempiamo tutte le stanze singole
    for _ in range(10):
        system.room_mgr.book_rooms("singola", 1)
    
    print(f"Capacità singola: {system.room_mgr.rooms['singola']['capacity']}, Prenotate: {system.room_mgr.rooms['singola']['booked']}")
    result_not_available = system.create_reservation("singola", 1, 5, False)
    print(f"Risultato: {result_not_available}")
    print(f"Stanze singole prenotate dopo tentativo fallito (stanze piene): {system.room_mgr.rooms.get('singola', {}).get('booked', 'Tipo stanza non trovato')}")
    print("-" * 20)

    # Esempio 3: Prenotazione con successo
    print(f"Tentativo prenotazione con successo:")
    # Resettiamo per un nuovo tentativo pulito se necessario, o usiamo un altro tipo di stanza
    # Assumiamo che ci siano stanze singole disponibili
    system_clean = BookingSystem() # Creiamo un nuovo sistema per testare uno scenario di successo puro
    print(f"Stanze singole disponibili all'inizio: {system_clean.room_mgr.check_availability('singola')}")
    result_success = system_clean.create_reservation("singola", 2, 3, False)
    print(f"Risultato: {result_success}")
    print(f"Stanze singole prenotate dopo successo: {system_clean.room_mgr.rooms.get('singola', {}).get('booked', 'Tipo stanza non trovato')}")
    print("-" * 20)