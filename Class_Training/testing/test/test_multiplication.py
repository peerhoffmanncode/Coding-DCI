import unittest
from math_operations import mul


class TestAddition(unittest.TestCase):
    def test_add(self):
        self.assertEqual(mul(2, 3), 6)


if __name__ == "__main__":
    unittest.main()
