# test_revisione.py
import pytest
from calcolatrice import somma, sottrazione, moltiplicazione, divisione

def test_somma_numeri_interi():
    assert somma(2, 3) == 5
    assert somma(-1, 1) == 0
    assert somma(0, 0) == 0
    assert somma(-5, -7) == -12

def test_somma_numeri_float():
    assert somma(2.5, 3.5) == 6.0
    assert somma(-1.5, 1.5) == 0.0
    assert somma(0.1, 0.2) == pytest.approx(0.3)
    assert somma(10.0, 0) == 10.0

def test_sottrazione_numeri_interi():
    assert sottrazione(5, 2) == 3
    assert sottrazione(2, 5) == -3
    assert sottrazione(10, 0) == 10
    assert sottrazione(-5, -2) == -3

def test_sottrazione_numeri_float():
    assert sottrazione(5.5, 2.0) == 3.5
    assert sottrazione(2.0, 5.5) == -3.5
    assert sottrazione(10.0, 0.0) == 10.0
    assert sottrazione(0.5, 0.1) == pytest.approx(0.4)

def test_moltiplicazione_numeri_interi():
    assert moltiplicazione(2, 3) == 6
    assert moltiplicazione(-2, 3) == -6
    assert moltiplicazione(0, 5) == 0
    assert moltiplicazione(-4, -5) == 20

def test_moltiplicazione_numeri_float():
    assert moltiplicazione(2.5, 2.0) == 5.0
    assert moltiplicazione(-1.5, 2.0) == -3.0
    assert moltiplicazione(0.5, 0.5) == pytest.approx(0.25)
    assert moltiplicazione(10.0, 0) == 0.0

def test_divisione_numeri_interi():
    assert divisione(6, 3) == 2.0
    assert divisione(7, 2) == 3.5
    assert divisione(-10, 2) == -5.0
    assert divisione(0, 5) == 0.0

def test_divisione_numeri_float():
    assert divisione(6.0, 3.0) == 2.0
    assert divisione(7.5, 2.5) == 3.0
    assert divisione(1.0, 3.0) == pytest.approx(0.3333333333333333)

def test_divisione_per_zero():
    with pytest.raises(ZeroDivisionError, match="Impossibile dividere per zero"):
        divisione(10, 0)
    with pytest.raises(ZeroDivisionError, match="Impossibile dividere per zero"):
        divisione(0, 0)