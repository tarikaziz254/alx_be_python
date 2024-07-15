import unittest
from simple_calculator import SimpleCalculator  

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()  

    def test_add(self):
        self.assertEqual(self.calc.add(1, 6), 7)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(1, 6), -5)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(1, 6), 6)

    def test_divide(self):
        self.assertEqual(self.calc.divide(6, 1), 6)
        with self.assertRaises(ValueError):
            self.calc.divide(6, 0)

if __name__ == "__main__":
    unittest.main()
