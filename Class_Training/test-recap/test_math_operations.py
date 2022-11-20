## ToDo:
# strict TDD

import unittest
from math_operations import add, sub


class MathTest(unittest.TestCase):
    def test_add(self):
        result = add(2, 2)
        expected_result = 4
        # assertions
        self.assertEqual(result, expected_result, "This does not work properly")

    def test_subtract(self):
        result = sub(2, 2)
        expected_result = 0
        # assertions
        self.assertEqual(result, expected_result)
