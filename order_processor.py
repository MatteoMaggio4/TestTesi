import sys

# Mock delle classi da altri file per isolare il test di UserManager e Inventory
class MockUserManager:
    def __init__(self):
        self.users = {
            "mario80": {"balance": 150.0},
            "luigi99": {"balance": 50.0}
        }

    def can_afford(self, username, amount):
        """Verifica se l'utente ha abbastanza saldo."""
        if username not in self.users:
            return False
        
        user_balance = self.users[username]["balance"]
        
        # BUG LOGICO 1: L'utente dovrebbe poter permettersi l'acquisto se il saldo è MAGGIORE O UGUALE all'importo.
        # Attualmente, fallisce se il saldo è esattamente uguale all'importo (es. 50.0 per un acquisto di 50.0).
        # CORREZIONE: Cambiato l'operatore da > a >=
        if user_balance >= amount: 
            return True
        return False

    def deduct_balance(self, username, amount):
        """Deduce l'importo dal saldo dell'utente."""
        if self.can_afford(username, amount):
            self.users[username]["balance"] -= amount
            return True
        return False

class MockInventory:
    def __init__(self):
        self.products = {
            "laptop": {"stock": 5, "price": 1000.0},
            "mouse": {"stock": 10, "price": 25.0},
            "keyboard": {"stock": 0, "price": 45.0} # Esaurito
        }

    def is_in_stock(self, product_name):
        if product_name in self.products and self.products[product_name]["stock"] > 0:
            return True
        return False

    def get_price(self, product_name):
        if product_name in self.products:
            return self.products[product_name]["price"]
        return 0.0

    def reduce_stock(self, product_name):
        if self.is_in_stock(product_name):
            self.products[product_name]["stock"] -= 1
            return True
        return False

class OrderProcessor:
    def __init__(self):
        self.user_mgr = MockUserManager()
        self.inventory = MockInventory()

    def process_order(self, username, product_name):
        if not self.inventory.is_in_stock(product_name):
            return "Fallito: Prodotto non disponibile"
            
        price = self.inventory.get_price(product_name)
        
        if self.user_mgr.can_afford(username, price):
             self.inventory.reduce_stock(product_name)
             self.user_mgr.deduct_balance(username, price)
             return "Successo: Ordine completato"
        else:
             return "Fallito: Saldo insufficiente"

# ----- Inizio Script di Test -----

passed_tests = 0
failed_tests = 0

def assert_equal(actual, expected, test_name):
    global passed_tests, failed_tests
    if actual == expected:
        print(f"[PASS] {test_name}")
        passed_tests += 1
    else:
        print(f"[FAIL] {test_name} - Atteso: {expected}, Ottenuto: {actual}")
        failed_tests += 1

def assert_true(condition, test_name):
    global passed_tests, failed_tests
    if condition:
        print(f"[PASS] {test_name}")
        passed_tests += 1
    else:
        print(f"[FAIL] {test_name} - La condizione non è vera")
        failed_tests += 1

def assert_false(condition, test_name):
    global passed_tests, failed_tests
    if not condition:
        print(f"[PASS] {test_name}")
        passed_tests += 1
    else:
        print(f"[FAIL] {test_name} - La condizione è vera ma ci si aspettava False")
        failed_tests += 1

# Test per il file user_manager.py (focus sul bug di can_afford)
print("--- Test per UserManager ---")
user_manager_instance = MockUserManager()

# Test 1: Saldo maggiore dell'importo
assert_true(user_manager_instance.can_afford("mario80", 100.0), "Test 1: Saldo maggiore dell'importo")

# Test 2: Saldo uguale all'importo (dopo fix)
assert_true(user_manager_instance.can_afford("luigi99", 50.0), "Test 2: Saldo uguale all'importo")

# Test 3: Saldo minore dell'importo
assert_false(user_manager_instance.can_afford("luigi99", 60.0), "Test 3: Saldo minore dell'importo")

# Test 4: Utente non esistente
assert_false(user_manager_instance.can_afford("wario", 10.0), "Test 4: Utente non esistente")

# Test 5: Deduce saldo con successo
initial_balance_mario = user_manager_instance.users["mario80"]["balance"]
assert_true(user_manager_instance.deduct_balance("mario80", 100.0), "Test 5: Deduce saldo con successo")
assert_equal(user_manager_instance.users["mario80"]["balance"], initial_balance_mario - 100.0, "Test 5.1: Saldo effettivamente dedotto")

# Test 6: Non deduce saldo con saldo insufficiente
initial_balance_luigi = user_manager_instance.users["luigi99"]["balance"]
assert_false(user_manager_instance.deduct_balance("luigi99", 60.0), "Test 6: Non deduce saldo con saldo insufficiente")
assert_equal(user_manager_instance.users["luigi99"]["balance"], initial_balance_luigi, "Test 6.1: Saldo non modificato con saldo insufficiente")

# Test 7: Deduce saldo con importo esatto
initial_balance_luigi_exact = user_manager_instance.users["luigi99"]["balance"]
assert_true(user_manager_instance.deduct_balance("luigi99", 50.0), "Test 7: Deduce saldo con importo esatto")
assert_equal(user_manager_instance.users["luigi99"]["balance"], initial_balance_luigi_exact - 50.0, "Test 7.1: Saldo diventa zero")


# Test per il file inventory.py (focus sul bug di reduce_stock)
print("\n--- Test per Inventory ---")
inventory_instance = MockInventory()

# Test 1: Verifica che reduce_stock diminuisca lo stock di un prodotto disponibile
inventory_instance.products["mouse"] = {"stock": 10, "price": 25.0}
initial_stock_mouse = inventory_instance.products["mouse"]["stock"]
inventory_instance.reduce_stock("mouse")
assert_equal(inventory_instance.products["mouse"]["stock"], initial_stock_mouse - 1, "Test 1: reduce_stock diminuisce lo stock correttamente")

# Test 2: Verifica che reduce_stock non modifichi lo stock di un prodotto esaurito
inventory_instance.products["keyboard"] = {"stock": 0, "price": 45.0}
initial_stock_keyboard = inventory_instance.products["keyboard"]["stock"]
inventory_instance.reduce_stock("keyboard")
assert_equal(inventory_instance.products["keyboard"]["stock"], initial_stock_keyboard, "Test 2: reduce_stock non modifica lo stock di prodotto esaurito")

# Test 3: Verifica che reduce_stock ritorni False per un prodotto non presente
initial_stock_monitor = inventory_instance.products.get("monitor", {}).get("stock", None)
assert_false(inventory_instance.reduce_stock("monitor"), "Test 3: reduce_stock ritorna False per prodotto non presente")
assert_equal(inventory_instance.products.get("monitor", {}).get("stock", None), initial_stock_monitor, "Test 3.1: reduce_stock non crea il prodotto se non presente")


# Test per il file order_processor.py (includendo il fix logico implicito per il deduct_balance)
print("\n--- Test per OrderProcessor ---")
order_processor_instance = OrderProcessor()

# Test 4: Ordine di un prodotto disponibile con saldo sufficiente
assert_equal(order_processor_instance.process_order("mario80", "mouse"), "Successo: Ordine completato", "Test 4: Ordine di mouse per mario80 va a buon fine")
assert_equal(order_processor_instance.inventory.products["mouse"]["stock"], 9, "Test 4.1: Stock del mouse decrementato correttamente")
assert_equal(order_processor_instance.user_mgr.users["mario80"]["balance"], 125.0, "Test 4.2: Saldo di mario80 decrementato correttamente")

# Test 5: Ordine di un prodotto non disponibile
assert_equal(order_processor_instance.process_order("mario80", "tablet"), "Fallito: Prodotto non disponibile", "Test 5: Ordine di tablet non disponibile")
assert_equal(order_processor_instance.user_mgr.users["mario80"]["balance"], 125.0, "Test 5.1: Saldo di mario80 non modificato per prodotto non disponibile")

# Test 6: Ordine di un prodotto con saldo insufficiente
order_processor_instance.inventory.products["console"] = {"stock": 1, "price": 200.0}
assert_equal(order_processor_instance.process_order("luigi99", "console"), "Fallito: Saldo insufficiente", "Test 6: Ordine di console per luigi99 con saldo insufficiente")
assert_equal(order_processor_instance.inventory.products["console"]["stock"], 1, "Test 6.1: Stock della console non modificato per saldo insufficiente")
assert_equal(order_processor_instance.user_mgr.users["luigi99"]["balance"], 50.0, "Test 6.2: Saldo di luigi99 non modificato per saldo insufficiente")

# Test 7: Ordine di un prodotto esaurito
assert_equal(order_processor_instance.process_order("mario80", "keyboard"), "Fallito: Prodotto non disponibile", "Test 7: Ordine di keyboard esaurita")
assert_equal(order_processor_instance.user_mgr.users["mario80"]["balance"], 125.0, "Test 7.1: Saldo di mario80 non modificato per prodotto esaurito")

# Test 8: Ordine con saldo esatto per un prodotto disponibile
order_processor_instance.inventory.products["pen"] = {"stock": 1, "price": 50.0}
assert_equal(order_processor_instance.process_order("luigi99", "pen"), "Successo: Ordine completato", "Test 8: Ordine di pen per luigi99 con saldo esatto va a buon fine")
assert_equal(order_processor_instance.inventory.products["pen"]["stock"], 0, "Test 8.1: Stock della pen decrementato correttamente")
assert_equal(order_processor_instance.user_mgr.users["luigi99"]["balance"], 0.0, "Test 8.2: Saldo di luigi99 diventa zero dopo acquisto esatto")


# Stampa metriche finali
print(f"\nPassed: {passed_tests}")
print(f"Failed: {failed_tests}")

if failed_tests > 0:
    sys.exit(1)
else:
    sys.exit(0)