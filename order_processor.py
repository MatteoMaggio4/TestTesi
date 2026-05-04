# test_order_processor.py
import sys

# Assumiamo che user_manager.py sia stato corretto per includere deduct_balance e l'utente 'peach'
from inventory import Inventory
from user_manager import UserManager # Assumiamo che UserManager sia disponibile e corretta
from order_processor import OrderProcessor


# Helper function to simulate adding/modifying user for tests if UserManager is accessible
# This is a placeholder assuming UserManager has a way to be configured for tests.
# If UserManager's internal structure is fixed, this might need adaptation.
def setup_user_for_test(user_mgr, username, balance):
    # Si assume che UserManager abbia un metodo per impostare il saldo di un utente esistente.
    # Se UserManager non espone direttamente il dizionario users, questa logica dovrà essere adattata
    # per utilizzare un'API pubblica di UserManager (es. user_mgr.set_balance(username, balance)).
    # Per ora, modifichiamo direttamente se la struttura è nota.
    if username in user_mgr.users:
        user_mgr.users[username]["balance"] = balance
    else:
        # Questo caso dovrebbe essere gestito in modo appropriato da UserManager se necessario
        # per i test che richiedono la creazione di utenti.
        print(f"Attenzione: Utente '{username}' non trovato in setup_user_for_test. Potrebbe essere necessario aggiungere l'utente.")
        # In un test reale, potresti voler aggiungere l'utente se non esiste:
        # user_mgr.add_user(username, balance=balance)


def test_successful_order():
    """Verifica che un ordine riuscito riduca stock e detragga il saldo."""
    processor = OrderProcessor()
    # Assicuriamoci che mario80 abbia un saldo iniziale sufficiente e leggiamolo
    initial_mario_balance = processor.user_mgr.users["mario80"]["balance"]
    initial_mouse_stock = processor.inventory.products["mouse"]["stock"]
    mouse_price = processor.inventory.get_price("mouse")

    # Esegui l'ordine
    result = processor.process_order("mario80", "mouse")

    # Controlla il risultato dell'ordine
    assert result == "Successo: Ordine completato", f"Test '{sys._getframe().f_code.co_name}' FAILED: Atteso 'Successo: Ordine completato', ottenuto '{result}'"

    # Verifica che il saldo sia stato detratto correttamente
    expected_balance = initial_mario_balance - mouse_price
    actual_balance = processor.user_mgr.users["mario80"]["balance"]
    assert actual_balance == expected_balance, \
        f"Test '{sys._getframe().f_code.co_name}' FAILED: Il saldo di Mario dovrebbe essere detratto. Atteso {expected_balance}, ottenuto {actual_balance}"

    # Verifica che la giacenza sia stata ridotta
    expected_stock = initial_mouse_stock - 1
    actual_stock = processor.inventory.products["mouse"]["stock"]
    assert actual_stock == expected_stock, \
        f"Test '{sys._getframe().f_code.co_name}' FAILED: La giacenza del mouse dovrebbe essere ridotta. Atteso {expected_stock}, ottenuto {actual_stock}"
    print(f"Test '{sys._getframe().f_code.co_name}' PASSED.")

def test_order_out_of_stock():
    """Verifica che un ordine fallisca se il prodotto è esaurito."""
    processor = OrderProcessor()
    initial_mario_balance = processor.user_mgr.users["mario80"]["balance"]
    initial_keyboard_stock = processor.inventory.products["keyboard"]["stock"] # 0

    result = processor.process_order("mario80", "keyboard")

    assert result == "Fallito: Prodotto non disponibile", f"Test '{sys._getframe().f_code.co_name}' FAILED: Atteso 'Fallito: Prodotto non disponibile', ottenuto '{result}'"
    # Verifica che il saldo non sia cambiato
    assert processor.user_mgr.users["mario80"]["balance"] == initial_mario_balance, \
        f"Test '{sys._getframe().f_code.co_name}' FAILED: Il saldo di Mario non dovrebbe cambiare. Atteso {initial_mario_balance}, ottenuto {processor.user_mgr.users['mario80']['balance']}"
    # Verifica che la giacenza non sia cambiata
    assert processor.inventory.products["keyboard"]["stock"] == initial_keyboard_stock, \
        f"Test '{sys._getframe().f_code.co_name}' FAILED: La giacenza della tastiera non dovrebbe cambiare. Atteso {initial_keyboard_stock}, ottenuto {processor.inventory.products['keyboard']['stock']}"
    print(f"Test '{sys._getframe().f_code.co_name}' PASSED.")

def test_order_insufficient_balance():
    """Verifica che un ordine fallisca se l'utente ha saldo insufficiente."""
    processor = OrderProcessor()
    initial_luigi_balance = processor.user_mgr.users["luigi99"]["balance"] # 50.0
    initial_laptop_stock = processor.inventory.products["laptop"]["stock"] # 5
    laptop_price = processor.inventory.get_price("laptop") # 1000.0

    result = processor.process_order("luigi99", "laptop")

    assert result == "Fallito: Saldo insufficiente", f"Test '{sys._getframe().f_code.co_name}' FAILED: Atteso 'Fallito: Saldo insufficiente', ottenuto '{result}'"
    # Verifica che il saldo non sia cambiato
    assert processor.user_mgr.users["luigi99"]["balance"] == initial_luigi_balance, \
        f"Test '{sys._getframe().f_code.co_name}' FAILED: Il saldo di Luigi non dovrebbe cambiare. Atteso {initial_luigi_balance}, ottenuto {processor.user_mgr.users['luigi99']['balance']}"
    # Verifica che la giacenza non sia cambiata
    assert processor.inventory.products["laptop"]["stock"] == initial_laptop_stock, \
        f"Test '{sys._getframe().f_code.co_name}' FAILED: La giacenza del laptop non dovrebbe cambiare. Atteso {initial_laptop_stock}, ottenuto {processor.inventory.products['laptop']['stock']}"
    print(f"Test '{sys._getframe().f_code.co_name}' PASSED.")

def test_order_exact_balance_match():
    """Verifica che un ordine riesca quando il saldo dell'utente è esattamente pari al prezzo."""
    processor = OrderProcessor()

    # --- CORREZIONE PER GESTIRE UTENTE E SALDO ---
    # Utilizziamo 'mario80' e impostiamo un saldo preciso per il test.
    # Per garantire che la modifica del saldo sia effettiva per l'istanza di UserManager
    # utilizzata da OrderProcessor, utilizziamo direttamente l'istanza di UserManager
    # dall'oggetto OrderProcessor stesso.
    user_to_test = "mario80"
    product_for_test = "mouse"
    
    mouse_price = processor.inventory.get_price(product_for_test)
    
    # Imposta il saldo di mario80 esattamente al prezzo del mouse per questo test.
    # Utilizziamo l'istanza di user_mgr da processor per assicurarci che la modifica sia valida.
    initial_balance_for_test = mouse_price
    
    # Assicuriamoci che l'utente esista prima di provare a impostare il saldo.
    if user_to_test not in processor.user_mgr.users:
        # Se l'utente non esiste, potrebbe essere necessario crearlo a seconda del setup di UserManager.
        # Per questo esempio, assumiamo che mario80 esista come nell'esempio originale.
        print(f"ERRORE nel test '{sys._getframe().f_code.co_name}': Utente '{user_to_test}' non trovato nel UserManager.")
        assert False, f"Utente '{user_to_test}' non trovato per eseguire il test."
    
    # Impostazione diretta del saldo sull'istanza di UserManager di OrderProcessor
    processor.user_mgr.users[user_to_test]["balance"] = initial_balance_for_test
    
    initial_user_balance = processor.user_mgr.users[user_to_test]["balance"]
    initial_product_stock = processor.inventory.products[product_for_test]["stock"]
    # --- FINE CORREZIONE ---

    result = processor.process_order(user_to_test, product_for_test)

    assert result == "Successo: Ordine completato", f"Test '{sys._getframe().f_code.co_name}' FAILED: Atteso 'Successo: Ordine completato' per saldo esatto, ottenuto '{result}'"
    
    # Verifica che il saldo sia stato detratto correttamente (dovrebbe essere 0)
    expected_balance = initial_user_balance - mouse_price
    actual_balance = processor.user_mgr.users[user_to_test]["balance"]
    assert actual_balance == expected_balance, \
        f"Test '{sys._getframe().f_code.co_name}' FAILED: Il saldo di {user_to_test} dovrebbe essere detratto. Atteso {expected_balance}, ottenuto {actual_balance}"
        
    # Verifica che la giacenza sia stata ridotta
    expected_stock = initial_product_stock - 1
    actual_stock = processor.inventory.products[product_for_test]["stock"]
    assert actual_stock == expected_stock, \
        f"Test '{sys._getframe().f_code.co_name}' FAILED: La giacenza del {product_for_test} dovrebbe essere ridotta. Atteso {expected_stock}, ottenuto {actual_stock}"
    print(f"Test '{sys._getframe().f_code.co_name}' PASSED.")

def test_order_nonexistent_product():
    """Verifica che un ordine fallisca per un prodotto inesistente."""
    processor = OrderProcessor()
    initial_mario_balance = processor.user_mgr.users["mario80"]["balance"]

    result = processor.process_order("mario80", "prodotto_inesistente")

    assert result == "Fallito: Prodotto non disponibile", f"Test '{sys._getframe().f_code.co_name}' FAILED: Atteso 'Fallito: Prodotto non disponibile', ottenuto '{result}'"
    # Verifica che il saldo non sia cambiato
    assert processor.user_mgr.users["mario80"]["balance"] == initial_mario_balance, \
        f"Test '{sys._getframe().f_code.co_name}' FAILED: Il saldo di Mario non dovrebbe cambiare. Atteso {initial_mario_balance}, ottenuto {processor.user_mgr.users['mario80']['balance']}"
    print(f"Test '{sys._getframe().f_code.co_name}' PASSED.")

def test_order_nonexistent_user():
    """Verifica che un ordine fallisca per un utente inesistente."""
    processor = OrderProcessor()
    initial_mouse_stock = processor.inventory.products["mouse"]["stock"]

    # Toad non è in UserManager nel setup predefinito
    result = processor.process_order("toad", "mouse") 

    # L'OrderProcessor chiama user_mgr.can_afford. Se user_mgr.can_afford('toad', price)
    # restituisce False per utente non esistente, l'OrderProcessor ritorna "Saldo insufficiente".
    # Questo è il comportamento attuale e va verificato.
    assert result == "Fallito: Saldo insufficiente", f"Test '{sys._getframe().f_code.co_name}' FAILED: Atteso 'Fallito: Saldo insufficiente', ottenuto '{result}'"
    
    # Verifica che la giacenza non sia cambiata
    assert processor.inventory.products["mouse"]["stock"] == initial_mouse_stock, \
        f"Test '{sys._getframe().f_code.co_name}' FAILED: La giacenza del mouse non dovrebbe cambiare. Atteso {initial_mouse_stock}, ottenuto {processor.inventory.products['mouse']['stock']}"
    print(f"Test '{sys._getframe().f_code.co_name}' PASSED.")


def run_tests():
    tests = [
        test_successful_order,
        test_order_out_of_stock,
        test_order_insufficient_balance,
        test_order_exact_balance_match,
        test_order_nonexistent_product,
        test_order_nonexistent_user,
    ]

    passed_count = 0
    failed_count = 0

    print("Running tests for OrderProcessor...\n")

    for test in tests:
        try:
            test()
            passed_count += 1
        except AssertionError as e:
            print(f"Test FAILED: {test.__name__} - {e}")
            failed_count += 1
        except Exception as e:
            print(f"Errore inaspettato nel test {test.__name__}: {e}")
            failed_count += 1
        print("-" * 30)

    print(f"\nPassed: {passed_count}")
    print(f"Failed: {failed_count}")

    if failed_count > 0:
        sys.exit(1)
    else:
        sys.exit(0)

if __name__ == "__main__":
    run_tests()