import copy
import unittest
from utils import list_generator
from selectionsort import selection_sort
from insertionsort import insertion_sort
from bubblesort import bubble_sort
from mergesort import merge_sort
from quicksort import quick_sort
from countingsort import counting_sort
from radixsort import radix_sort


class SortingTests(unittest.TestCase):
    def setUp(self) -> None:
        """Create random list of integers"""
        self.test_array = list_generator(10000)

    def sorted(self, array) -> bool:
        """Check if list is sorted in ascending order"""
        for i in range(len(array)-1):
            self.assertTrue(array[i] <= array[i+1])
        return True

    def testSelectionSort(self):
        test = copy.deepcopy(self.test_array)
        result = selection_sort(test)
        self.sorted(result)

    def testInsertionSort(self):
        test = copy.deepcopy(self.test_array)
        result = insertion_sort(test)
        self.sorted(result)

    def testBubbleSort(self):
        test = copy.deepcopy(self.test_array)
        result = bubble_sort(test)
        self.sorted(result)

    def testQuickSort(self):
        test = copy.deepcopy(self.test_array)
        result = quick_sort(test)
        self.sorted(result)

    def testMergeSort(self):
        test = copy.deepcopy(self.test_array)
        result = merge_sort(test)
        self.sorted(result)

    def testCountSort(self):
        test = copy.deepcopy(self.test_array)
        result = counting_sort(test)
        self.sorted(result)

    def testRadixSort(self):
        test = copy.deepcopy(self.test_array)
        result = radix_sort(test)
        self.sorted(result)


if __name__ == '__main__':
    unittest.main()
