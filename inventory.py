# test_inventory_basic.py
import sys

class Inventory:
    def __init__(self):
        # Database in memoria simulato
        self.products = {
            "laptop": {"stock": 5, "price": 1000.0},
            "mouse": {"stock": 10, "price": 25.0},
            "keyboard": {"stock": 0, "price": 45.0} # Esaurito
        }

    def is_in_stock(self, product_name):
        """Verifica se il prodotto è in magazzino."""
        # Un prodotto è in stock se esiste e la sua giacenza è maggiore di 0
        return product_name in self.products and self.products[product_name]["stock"] > 0

    def get_price(self, product_name):
        if product_name in self.products:
            return self.products[product_name]["price"]
        return 0.0

    def reduce_stock(self, product_name):
        """
        Riduce la giacenza di un prodotto di 1 unità.
        Ritorna True se la giacenza è stata effettivamente ridotta, False altrimenti.
        """
        # Controllo se il prodotto esiste e se è in stock prima di decrementare
        if product_name in self.products and self.products[product_name]["stock"] > 0:
            self.products[product_name]["stock"] -= 1
            return True
        return False


# --- Funzioni di supporto per i test (sostituiscono TestRunner) ---

# Variabili globali per tenere traccia dei risultati dei test
_passed_count = 0
_failed_count = 0

def _assert_equal(actual, expected, message=""):
    global _failed_count
    if actual != expected:
        _failed_count += 1
        print(f"  FAILED: Assertion failed: Expected {expected}, got {actual}. {message}")
        return False
    return True

def _assert_true(condition, message=""):
    global _failed_count
    if not condition:
        _failed_count += 1
        print(f"  FAILED: Assertion failed: Condition is not true. {message}")
        return False
    return True

def _assert_false(condition, message=""):
    global _failed_count
    if condition:
        _failed_count += 1
        print(f"  FAILED: Assertion failed: Condition is true. {message}")
        return False
    return True

def _run_test(test_name, test_func):
    global _passed_count, _failed_count
    print(f"Running test: {test_name}")
    try:
        if test_func(): # La funzione di test ritorna True se supera, False se fallisce
            print(f"  PASSED")
            _passed_count += 1
        # Se la funzione di test ritorna False, il messaggio di fallimento è già stato stampato da _assert_*
    except Exception as e:
        _failed_count += 1
        print(f"  FAILED: Exception during test execution: {e}")
        # Non uscire immediatamente, continua con gli altri test

# --- Test Functions ---
def test_initial_stock_correct():
    inventory = Inventory()
    if not _assert_equal(inventory.products["laptop"]["stock"], 5, "Initial stock for laptop is incorrect."): return False
    if not _assert_equal(inventory.products["mouse"]["stock"], 10, "Initial stock for mouse is incorrect."): return False
    if not _assert_equal(inventory.products["keyboard"]["stock"], 0, "Initial stock for keyboard is incorrect."): return False
    return True

def test_get_price_correct():
    inventory = Inventory()
    if not _assert_equal(inventory.get_price("laptop"), 1000.0, "Price for laptop is incorrect."): return False
    if not _assert_equal(inventory.get_price("mouse"), 25.0, "Price for mouse is incorrect."): return False
    if not _assert_equal(inventory.get_price("keyboard"), 45.0, "Price for keyboard is incorrect."): return False
    if not _assert_equal(inventory.get_price("monitor"), 0.0, "Price for non-existent product should be 0.0."): return False
    return True

def test_reduce_stock_successful_for_in_stock_item():
    inventory = Inventory()
    initial_stock = inventory.products["mouse"]["stock"]
    result = inventory.reduce_stock("mouse")
    if not _assert_true(result, "reduce_stock should return True for an in-stock item."): return False
    if not _assert_equal(inventory.products["mouse"]["stock"], initial_stock - 1, "Stock should be decremented by 1."): return False
    return True

def test_reduce_stock_fails_for_out_of_stock_item():
    inventory = Inventory()
    initial_stock = inventory.products["keyboard"]["stock"]
    result = inventory.reduce_stock("keyboard")
    if not _assert_false(result, "reduce_stock should return False for an out-of-stock item."): return False
    if not _assert_equal(inventory.products["keyboard"]["stock"], initial_stock, "Stock should not be decremented for an out-of-stock item."): return False
    return True

def test_is_in_stock_correctly_identifies_in_stock():
    inventory = Inventory()
    if not _assert_true(inventory.is_in_stock("laptop"), "Laptop should be identified as in stock."): return False
    return True

def test_is_in_stock_correctly_identifies_out_of_stock():
    inventory = Inventory()
    if not _assert_false(inventory.is_in_stock("keyboard"), "Keyboard should be identified as out of stock."): return False
    return True

def test_is_in_stock_correctly_identifies_nonexistent():
    inventory = Inventory()
    if not _assert_false(inventory.is_in_stock("monitor"), "Non-existent product should be identified as not in stock."): return False
    return True

def test_reduce_stock_multiple_times_to_zero():
    inventory = Inventory()
    product_name = "mouse"
    initial_stock = inventory.products[product_name]["stock"]
    
    # Riduci stock fino a 1 unità
    for _ in range(initial_stock - 1):
        if not inventory.reduce_stock(product_name):
            return _assert_false(False, f"Failed to reduce stock for {product_name} before reaching 1.")
            
    if not _assert_equal(inventory.products[product_name]["stock"], 1, "Stock should be 1 before the last reduction."): return False

    # Riduci stock all'ultima unità
    if not inventory.reduce_stock(product_name):
        return _assert_false(False, f"Failed to reduce stock for {product_name} to 0.")
    if not _assert_equal(inventory.products[product_name]["stock"], 0, "Stock should be 0 after the last reduction."): return False

    # Tenta di ridurre ulteriormente lo stock
    if not _assert_false(inventory.reduce_stock(product_name), f"Reducing stock for {product_name} when it's 0 should fail."): return False
    if not _assert_equal(inventory.products[product_name]["stock"], 0, "Stock should remain 0 after failed reduction attempt."): return False
    return True


# --- Esecuzione dei test ---
if __name__ == "__main__":
    print("--- Running Inventory Basic Tests ---")
    _run_test("test_initial_stock_correct", test_initial_stock_correct)
    _run_test("test_get_price_correct", test_get_price_correct)
    _run_test("test_reduce_stock_successful_for_in_stock_item", test_reduce_stock_successful_for_in_stock_item)
    _run_test("test_reduce_stock_fails_for_out_of_stock_item", test_reduce_stock_fails_for_out_of_stock_item)
    _run_test("test_is_in_stock_correctly_identifies_in_stock", test_is_in_stock_correctly_identifies_in_stock)
    _run_test("test_is_in_stock_correctly_identifies_out_of_stock", test_is_in_stock_correctly_identifies_out_of_stock)
    _run_test("test_is_in_stock_correctly_identifies_nonexistent", test_is_in_stock_correctly_identifies_nonexistent)
    _run_test("test_reduce_stock_multiple_times_to_zero", test_reduce_stock_multiple_times_to_zero)


    print("\n--- Test Summary ---")
    total_tests = _passed_count + _failed_count
    print(f"Total tests: {total_tests}")
    print(f"Passed: {_passed_count}")
    print(f"Failed: {_failed_count}")

    if _failed_count > 0:
        print("SOME TESTS FAILED")
        sys.exit(1) # Esce con codice di errore se ci sono fallimenti
    else:
        print("ALL TESTS PASSED")
        sys.exit(0) # Esce con codice 0 se tutti i test sono passati