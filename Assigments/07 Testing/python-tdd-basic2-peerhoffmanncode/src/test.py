import unittest
from app import rnd, max_num_in_list
import re


class TestApp(unittest.TestCase):
    # check if max_num_in_list will return right value
    def test_max_num_in_list1(self):
        self.assertEqual(
            max_num_in_list([2, 6, 8, 7, -1]),
            8,
            "return value not the greatest value in max_num_in_list",
        )

    def test_rnd_1(self):
        """this test is valid to check if a function will
        correctly return a random number within a given range for one given moment!
        This will NOT prove it will never be out of range!"""
        self.assertIn(rnd(2, 20), range(2, 21))

    def test_rnd_2(self):
        """this test is valid to check if a function will
        correctly return a random number within a given range!
        This will ONLY prove it will not be out of range for that given moment!"""
        rnd_num = rnd(2, 20)
        self.assertGreaterEqual(rnd_num, 2)  # check lower bound
        self.assertLessEqual(rnd_num, 20)  # check upper bound

    def test_rnd_3(self):
        """this test is valid to check if a function will correctly
        return a random number within a given range!
        This will ONLY prove it will not be out of range for that given moment!"""

        rnd_num = rnd(2, 20)
        if rnd_num < 2 or rnd_num > 20:
            self.fail("Out of range!")


if __name__ == "__main__":
    unittest.main()
