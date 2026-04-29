Nessun bug

## UNIT TEST
```python
import pytest
from sconto import applica_sconto

def test_applica_sconto_basico_valido():
    # Test caso base: sconto positivo valido
    prezzo_base = 100
    sconto = 10
    expected_prezzo_finale = 90
    assert applica_sconto(prezzo_base, sconto) == expected_prezzo_finale
```

DEPENDENCIES: pytest
TEST_FILE_NAME: test_sconto.py
RUN_COMMAND: pytest test_sconto.py