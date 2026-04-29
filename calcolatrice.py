def applica_sconto(prezzo_base, sconto):
    # BUG LOGICO: somma invece di sottrarre
    prezzo_finale = prezzo_base + sconto
    return prezzo_finale