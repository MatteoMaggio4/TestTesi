import pytest
from calcolatrice import somma, sottrazione, moltiplicazione, divisione

def test_somma_interi():
    assert somma(2, 3) == 5

def test_somma_float():
    assert somma(2.5, 3.5) == 6.0

def test_somma_misti():
    assert somma(2, 3.5) == 5.5

def test_sottrazione_interi():
    assert sottrazione(5, 2) == 3

def test_sottrazione_float():
    assert sottrazione(5.5, 2.0) == 3.5

def test_sottrazione_negativi():
    assert sottrazione(5, 10) == -5

def test_moltiplicazione_interi():
    assert moltiplicazione(2, 4) == 8

def test_moltiplicazione_float():
    assert moltiplicazione(2.5, 2.0) == 5.0

def test_moltiplicazione_zero():
    assert moltiplicazione(5, 0) == 0

def test_divisione_interi():
    assert divisione(10, 2) == 5.0

def test_divisione_float():
    assert divisione(10.0, 4.0) == 2.5

def test_divisione_restituisce_float():
    assert isinstance(divisione(10, 2), float)
    assert isinstance(divisione(10, 3), float)

def test_divisione_per_zero():
    with pytest.raises(ZeroDivisionError):
        divisione(10, 0)