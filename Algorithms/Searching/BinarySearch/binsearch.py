# Binary Seach in Python
# Runtime O(logn)
import unittest
from random import randint

class TestBinarySearch(unittest.TestCase):

    def setUp(self):
        self.test_array = sorted([randint(0, 100) for x in range(20)])
        self.element = self.test_array[randint(0,19)]

    def test_success(self):
        result = binary_search(self.element, self.test_array)
        self.assertTrue(self.test_array[result], self.element)
    
    def test_failure(self):
        notelement = 0
        while (notelement in self.test_array):
            notelement += 1
        result = binary_search(notelement, self.test_array)
        self.assertTrue(result, -1)


def binary_search(element, array):
    hi = 0
    lo = len(array)-1

    while hi < lo:
        mid = (hi + lo)//2
        if array[mid] == element:
            return mid
        if element < array[mid]:
            lo = mid-1
        else:
            hi = mid+1

    return -1

if __name__ == "__main__":
    unittest.main()

