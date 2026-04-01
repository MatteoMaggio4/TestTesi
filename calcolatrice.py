# calcolatrice.py
"""
Un modulo che fornisce funzioni base per operazioni aritmetiche:
somma, sottrazione, moltiplicazione e divisione.
"""

def somma(a: int | float, b: int | float) -> int | float:
    """
    Esegue la somma di due numeri.
    """
    return a + b

def sottrazione(a: int | float, b: int | float) -> int | float:
    """
    Esegue la sottrazione di due numeri.
    """
    return a - b

def moltiplicazione(a: int | float, b: int | float) -> int | float:
    """
    Esegue la moltiplicazione di due numeri.
    """
    return a * b

def divisione(a: int | float, b: int | float) -> float:
    """
    Esegue la divisione di due numeri.
    Solleva ZeroDivisionError se il divisore è zero.
    """
    if b == 0:
        raise ZeroDivisionError("Impossibile dividere per zero") # Modifica: ora solleva ZeroDivisionError
    return a / b