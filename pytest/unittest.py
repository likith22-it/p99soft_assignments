import unittest

def add(a, b):
    return a + b

def is_even(n):
    return n % 2 == 0

def get_user():
    return {"name": "likith", "age": 22}

def find_item(lst, item):
    return item if item in lst else None

def return_none():
    return None



class TestFunctions(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)   # a == b

    def test_is_even_true(self):
        self.assertTrue(is_even(4))      # bool(x) is True

    def test_is_even_false(self):
        self.assertFalse(is_even(5))     # bool(x) is False

    def test_instance(self):
        self.assertIsInstance(get_user(), dict)  # isinstance(a, b)

    def test_is_none(self):
        self.assertIsNone(return_none())  # x is None

    def test_is_identity(self):
        a = [1, 2]
        b = a
        self.assertIs(a, b)              # a is b (same object)

    def test_in(self):
        self.assertIn("likith", get_user().values())  # a in b


# Run tests
if __name__ == "__main__":
    unittest.main()