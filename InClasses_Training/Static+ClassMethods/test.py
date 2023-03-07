import unittest
from stuff import add


class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(add(1, 1), 2)
