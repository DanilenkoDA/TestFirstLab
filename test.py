import unittest
import app 


class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(app.add(1, 2), 3)
        self.assertEqual(app.add(1, -5), -4)
        self.assertEqual(app.add(-15, 1), -14)
        self.assertEqual(app.add(0.0, 1), 1)
        self.assertEqual(app.add(1, 1), 2)
        
    def test_subtract(self): 
        self.assertEqual(app.subtract(1, 2), -1)
        self.assertEqual(app.subtract(1, -1000000), 1000001)
        self.assertEqual(app.subtract(1, 50), -49)
        self.assertEqual(app.subtract(0.5, -0.75), 1.25)
        self.assertEqual(app.subtract(0, 0), 0)

    def test_multiply(self):
        self.assertEqual(app.multiply(2, 2), 4)
        self.assertEqual(app.multiply(2, -1), -2)
        self.assertEqual(app.multiply(2, 0), 0)
        self.assertEqual(app.multiply(0.5, 0.25), 0.125)
        self.assertEqual(app.multiply(-2, -2), 4)

    def test_divide(self):
        with self.assertRaises(ValueError):
            app.divide(5, 0)
        self.assertEqual(app.divide(5, 1), 5)
        self.assertEqual(app.divide(-1, 1), -1)
        self.assertEqual(app.divide(2, 4), 0.5)
        self.assertEqual(app.divide(1, 0.5), 2)

    def test_modulus(self):
        with self.assertRaises(ValueError):
            app.modulus(5, 0)
        self.assertEqual(app.modulus(5, 1), 0)
        self.assertEqual(app.modulus(1, 2), 1)
        self.assertEqual(app.modulus(-5, 3), 1)
        self.assertEqual(app.modulus(-6, -2), 0)

    def test_exponentiation(self):
        with self.assertRaises(ValueError):
            app.exponentiation(0, 0)
        self.assertEqual(app.exponentiation(5, 1), 5)
        self.assertEqual(app.exponentiation(2, 2), 4)
        self.assertEqual(app.exponentiation(-2, 2), 4)
        self.assertEqual(app.exponentiation(5, 0), 1)
        self.assertEqual(app.exponentiation(-2, -2), 0.25)

    def test_square_root(self):
        with self.assertRaises(ValueError):
            app.square_root(-5)
        self.assertEqual(app.square_root(4), 2)
        self.assertEqual(app.square_root(9), 3)
        self.assertEqual(app.square_root(0), 0)
        self.assertEqual(app.square_root(25), 5)


if __name__ == "__main__":
 unittest.main()
