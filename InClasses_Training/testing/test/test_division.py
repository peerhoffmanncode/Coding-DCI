import unittest
from math_operations import div


class TestAddition(unittest.TestCase):
    def test_add(self):
        self.assertEqual(div(6, 3), 2)


if __name__ == "__main__":
    unittest.main()
