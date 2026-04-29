Nessun bug

```python
## UNIT TEST
import unittest
from calcolatrice import somma, sottrazione, moltiplicazione, divisione

class TestCalcolatrice(unittest.TestCase):

    def test_somma(self):
        self.assertEqual(somma(5, 3), 8)
        self.assertEqual(somma(-1, 1), 0)
        self.assertEqual(somma(0, 0), 0)
        self.assertEqual(somma(10.5, 2.5), 13.0)

    def test_sottrazione(self):
        self.assertEqual(sottrazione(10, 4), 6)
        self.assertEqual(sottrazione(5, 5), 0)
        self.assertEqual(sottrazione(2, 7), -5)
        self.assertEqual(sottrazione(10.0, 3.5), 6.5)

    def test_moltiplicazione(self):
        self.assertEqual(moltiplicazione(2, 6), 12)
        self.assertEqual(moltiplicazione(5, 0), 0)
        self.assertEqual(moltiplicazione(-3, 4), -12)
        self.assertEqual(moltiplicazione(2.5, 2), 5.0)

    def test_divisione(self):
        self.assertEqual(divisione(10, 2), 5.0)
        self.assertEqual(divisione(7, 2), 3.5)
        self.assertEqual(divisione(-10, 5), -2.0)
        self.assertEqual(divisione(0, 5), 0.0)

    def test_divisione_per_zero(self):
        with self.assertRaises(ValueError) as cm:
            divisione(5, 0)
        self.assertEqual(str(cm.exception), "Cannot divide by zero.")

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)

```
DEPENDENCIES: NONE
TEST_FILE_NAME: test_calcolatrice.py
RUN_COMMAND: python -m unittest test_calcolatrice.py