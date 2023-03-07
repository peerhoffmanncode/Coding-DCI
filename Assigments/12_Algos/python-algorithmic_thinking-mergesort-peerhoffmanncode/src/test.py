import unittest
from mergesort import mergesort


class TestMergeSortAlgo(unittest.TestCase):
    def setUp(self):
        # unordered
        self.nums1 = [3, 7, 2, 8, 4, 6, 9, 1, 4]
        self.expect1 = [1, 2, 3, 4, 4, 6, 7, 8, 9]

        # wired ordered
        self.nums2 = [9, 8, 7, 6, 6, 7, 8, 9, 9]
        self.expect2 = [6, 6, 7, 7, 8, 8, 9, 9, 9]

        # already ordered !
        self.nums3 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.expect3 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def test_unordered(self):
        result = []
        result = mergesort(self.nums1)
        self.assertEqual(result, self.expect1)
        self.assertEqual(len(result), len(self.expect1))

    def test_wired_ordered(self):
        result = []
        result = mergesort(self.nums2)
        self.assertEqual(result, self.expect2)
        self.assertEqual(len(result), len(self.expect2))

    def test_already_ordered(self):
        result = []
        result = mergesort(self.nums3)
        self.assertEqual(result, self.expect3)
        self.assertEqual(len(result), len(self.expect3))
