import unittest
import calc

class testcalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc.add(10, 2),12)
        
    def test_subtract(self):
        self.assertEqual(calc.subtract(10, 2),8)

    def test_multiply(self):
        self.assertEqual(calc.multiply(10, 2),20)

    def test_divide(self):
        self.assertEqual(calc.divide(10, 2),5)

if __name__ == "__main__":
    unittest.main()