import unittest
from string_operations import make_full_name


class TestAddition(unittest.TestCase):
    def test_add(self):
        self.assertEqual(
            make_full_name(["victor", "nizar", "emily", "some other name"]),
            "victor nizar emily some other name",
        )
        self.assertDictContainsSubset


if __name__ == "__main__":
    unittest.main()
