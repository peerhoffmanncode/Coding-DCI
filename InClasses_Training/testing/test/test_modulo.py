import unittest
from math_operations import mod


class TestAddition(unittest.TestCase):
    def test_add(self):
        self.assertEqual(mod(5, 2), 1)


if __name__ == "__main__":
    unittest.main()
