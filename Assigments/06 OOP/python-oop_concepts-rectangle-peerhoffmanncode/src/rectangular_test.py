import unittest
from app import Rectangle


class TestRectangleMethods(unittest.TestCase):

    """Class to test Rectangle methods"""

    def test_get_area(self):
        self.assertEqual(Rectangle(1, 2).get_area(), 2)
        self.assertRaises(TypeError, Rectangle(None, None).get_area)

    def test_get_perimeter(self):
        self.assertEqual(Rectangle(1, 2).get_perimeter(), 6)

    def test_get_diagonal(self):
        self.assertEqual(Rectangle(3, 4).get_diagonal(), 5)

    def test_get_width(self):
        self.assertEqual(Rectangle(3, 4).get_width(), 3)

    def test_get_height(self):
        self.assertEqual(Rectangle(3, 4).get_height(), 4)


if __name__ == "__main__":
    unittest.main()
