import unittest
from operaciones import dividir

class Test_divisiones(unittest.TestCase):

    # prueba 1: un caso basico que deberia funcionar
    def test_division_exacta(self):
        self.assertEqual(dividir(10,2), 5)

    # prueba 2: probando con numeros deciamles 
    def test_division_con_decimales(self):
        self.assertEqual(dividir(5,2), 2.5)

    # prueba 3: el "caso limite" (edge case) 
    def test_division_por_cero(self):
        self.assertEqual(dividir(10, 0), "no es posible dividir entre 0")

if __name__ == '__main__':
    unittest.main()