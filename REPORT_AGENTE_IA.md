## ANALISI DELL'ERRORE
Le funzioni `somma` e `sottrazione` contengono un errore logico: la funzione `somma` esegue una sottrazione, e la funzione `sottrazione` esegue un'addizione. Le operazioni sono state invertite.

## CODICE CORRETTO

```python
def somma(a, b):
    return a + b

def sottrazione(a, b):
    return a - b
```

## UNIT TEST

```python
import pytest
from calcolatrice import somma, sottrazione

def test_somma_positivi():
    assert somma(2, 3) == 5
    assert somma(10, 0) == 10
    assert somma(1, 1) == 2

def test_somma_negativi():
    assert somma(-2, -3) == -5
    assert somma(-5, 2) == -3
    assert somma(5, -2) == 3

def test_somma_zero():
    assert somma(0, 0) == 0
    assert somma(10, 0) == 10
    assert somma(0, 10) == 10

def test_sottrazione_positivi():
    assert sottrazione(5, 3) == 2
    assert sottrazione(10, 0) == 10
    assert sottrazione(1, 1) == 0

def test_sottrazione_negativi():
    assert sottrazione(-5, -2) == -3
    assert sottrazione(-5, 2) == -7
    assert sottrazione(5, -2) == 7

def test_sottrazione_zero():
    assert sottrazione(0, 0) == 0
    assert sottrazione(10, 0) == 10
    assert sottrazione(0, 10) == -10
```

DEPENDENCIES: pytest
TEST_FILE_NAME: test_calcolatrice.py
RUN_COMMAND: pytest test_calcolatrice.py