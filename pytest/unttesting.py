import unittest

def add(x, y):
    return x + y

class TestCalculator(unittest.TestCase):
    def test_add(self):
        # Assertions check if actual results match expected values
        self.assertEqual(add(10, 5), 15)
        self.assertEqual(add(-1, 1), 0)

if __name__ == '__main__':
    unittest.main()
