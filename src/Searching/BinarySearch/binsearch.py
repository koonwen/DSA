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
    endIndex = len(array)-1
    startIndex = 0

    while startIndex < endIndex:
        middleIndex = (startIndex + endIndex)//2
        if array[middleIndex] == element:
            return middleIndex
        if element < array[middleIndex]:
            endIndex = middleIndex-1
        else:
            startIndex = middleIndex+1

    return -1


if __name__ == "__main__":
    unittest.main()
