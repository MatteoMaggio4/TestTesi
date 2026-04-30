Nessun bug

Non è stata riscontrata alcuna falla logica nel codice fornito. La logica per l'applicazione dello sconto e la gestione degli scenari di errore (sconto negativo o sconto maggiore del prezzo base) è implementata correttamente, come evidenziato anche dalle correzioni e dal test di contesto forniti.

## UNIT TEST

```python
import pytest
from sconto import applica_sconto

def test_applica_sconto_valore_normale():
    # Test di un'applicazione di sconto standard
    prezzo_base = 100
    sconto = 20
    expected_prezzo_finale = 80
    assert applica_sconto(prezzo_base, sconto) == expected_prezzo_finale

def test_applica_sconto_senza_sconto():
    # Test con sconto pari a zero
    prezzo_base = 50
    sconto = 0
    expected_prezzo_finale = 50
    assert applica_sconto(prezzo_base, sconto) == expected_prezzo_finale

def test_applica_sconto_totale():
    # Test con sconto pari al prezzo base (risultato zero)
    prezzo_base = 75
    sconto = 75
    expected_prezzo_finale = 0
    assert applica_sconto(prezzo_base, sconto) == expected_prezzo_finale

# Il test per lo sconto negativo è già presente nel contesto e copre correttamente la validazione.
# test_applica_sconto_valore_negativo in test_sconto.py

def test_applica_sconto_maggiore_del_prezzo_base():
    # Test sconto maggiore del prezzo base (dovrebbe sollevare un'eccezione)
    prezzo_base = 100
    sconto = 120
    with pytest.raises(ValueError, match="Lo sconto non può essere maggiore del prezzo base."):
        applica_sconto(prezzo_base, sconto)
```

DEPENDENCIES: [pytest]
TEST_FILE_NAME: test_sconto.py
RUN_COMMAND: pytest test_sconto.py