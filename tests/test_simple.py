import unittest

from src.VorGemeinde import Gemeinde


class TestArithmetic(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(Gemeinde.randomGemeinde(), "Altach")
if __name__ == '__main__':
    unittest.main()