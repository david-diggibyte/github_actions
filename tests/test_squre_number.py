import unittest
from src.square_number import square_number

class TestSquareNumber(unittest.TestCase):
    def test_square(self):
        self.assertEqual(square_number(5), 25)
        self.assertEqual(square_number(0), 0)
        self.assertEqual(square_number(-4), 16)
        self.assertEqual(square_number(1), 1)

if __name__ == "__main__":
    unittest.main()