Il `FILE TARGET: calcolatrice.py` non contiene codice, quindi non è possibile effettuare un'analisi su di esso.
L'analisi viene quindi eseguita sul file fornito come contesto, `sconto.py`, che presenta un bug logico esplicito.

---
## ANALISI DELL'ERRORE
Nel file `sconto.py`, la funzione `applica_sconto` ha lo scopo di calcolare il prezzo finale di un prodotto dopo aver applicato uno sconto. Tuttavia, l'implementazione attuale somma lo `sconto` al `prezzo_base` (`prezzo_finale = prezzo_base + sconto`). Questo è un errore logico, in quanto uno sconto dovrebbe ridurre il prezzo originale, non aumentarlo.

## CODICE CORRETTO
```python
# FILE TARGET: sconto.py (trattato come target per l'analisi del bug esplicito)
def applica_sconto(prezzo_base, sconto):
    # CORREZIONE: Sottrae lo sconto dal prezzo base
    if sconto < 0:
        raise ValueError("Lo sconto non può essere negativo.")
    if sconto > prezzo_base:
        raise ValueError("Lo sconto non può essere maggiore del prezzo base.")
    prezzo_finale = prezzo_base - sconto
    return prezzo_finale
```

## UNIT TEST
```python
# TEST_FILE_NAME: test_sconto.py
import pytest
from sconto import applica_sconto

def test_applica_sconto_base():
    # Test caso base: sconto positivo valido
    prezzo_base = 100
    sconto = 10
    expected_prezzo_finale = 90
    assert applica_sconto(prezzo_base, sconto) == expected_prezzo_finale

def test_applica_sconto_zero():
    # Test sconto zero
    prezzo_base = 50
    sconto = 0
    expected_prezzo_finale = 50
    assert applica_sconto(prezzo_base, sconto) == expected_prezzo_finale

def test_applica_sconto_massimo():
    # Test sconto pari al prezzo base
    prezzo_base = 75
    sconto = 75
    expected_prezzo_finale = 0
    assert applica_sconto(prezzo_base, sconto) == expected_prezzo_finale

def test_applica_sconto_con_decimali():
    # Test con valori decimali
    prezzo_base = 99.99
    sconto = 9.99
    # Usiamo pytest.approx per comparazioni float
    assert applica_sconto(prezzo_base, sconto) == pytest.approx(90.00)

def test_applica_sconto_valore_negativo():
    # Test sconto negativo (dovrebbe sollevare un'eccezione)
    prezzo_base = 100
    sconto = -5
    with pytest.raises(ValueError, match="Lo sconto non può essere negativo."):
        applica_sconto(prezzo_base, sconto)

def test_applica_sconto_maggiore_del_prezzo():
    # Test sconto maggiore del prezzo base (dovrebbe sollevare un'eccezione)
    prezzo_base = 50
    sconto = 60
    with pytest.raises(ValueError, match="Lo sconto non può essere maggiore del prezzo base."):
        applica_sconto(prezzo_base, sconto)
```

DEPENDENCIES: [pytest]
TEST_FILE_NAME: test_sconto.py
RUN_COMMAND: pytest test_sconto.py