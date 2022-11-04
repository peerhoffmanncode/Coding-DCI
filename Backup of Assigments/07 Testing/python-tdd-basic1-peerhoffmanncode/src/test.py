from text import to_upper, to_word_list_isupper
import unittest


class Test(unittest.TestCase):
    # Test1
    def test_to_upper(self):
        self.assertEqual(to_upper("abcdef"), "ABCDEF")

    # Test2
    def test_to_word_list_isupper_1(self):
        self.assertTrue(to_word_list_isupper(["I", "LOVE", "YOU"]))

    # Test3
    def test_to_word_list_isupper_2(self):
        self.assertFalse(to_word_list_isupper(["i", "LOVE", "YOU"]))

    # Test4
    def test_to_upper_2(self):
        with self.assertRaises(TypeError):
            to_upper(15)

    # Test5 part1
    def test_to_word_list_isupper_3(self):
        with self.assertRaises(TypeError):
            to_word_list_isupper([15, "hello"])

    # Test5 part2
    def test_to_word_list_isupper_4(self):
        with self.assertRaises(TypeError):
            to_word_list_isupper(15)


if __name__ == "__main__":
    unittest.main()
