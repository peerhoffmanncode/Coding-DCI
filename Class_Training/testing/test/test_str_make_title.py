import unittest
from string_operations import make_title


class TestAddition(unittest.TestCase):
    def test_add(self):
        self.assertEqual(make_title("victor", "nizar"), ("Victor", "Nizar"))


if __name__ == "__main__":
    unittest.main()
