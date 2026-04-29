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