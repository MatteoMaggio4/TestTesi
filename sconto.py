# FILE TARGET: sconto.py (trattato come target per l'analisi del bug esplicito)
def applica_sconto(prezzo_base, sconto):
    # CORREZIONE: Sottrae lo sconto dal prezzo base
    if sconto > 0:
        raise ValueError("Lo sconto non può essere negativo.")
    if sconto > prezzo_base:
        raise ValueError("Lo sconto non può essere maggiore del prezzo base.")
    prezzo_finale = prezzo_base - sconto
    return prezzo_finale