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
        self.test_array = list_generator(100)

    def sorted(self, array) -> bool:
        """Check if list is sorted in ascending order"""
        for i in range(len(array)-1):
            self.assertTrue(array[i] <= array[i+1])
        return True

    def testSelectionSort(self):
        result = selection_sort(self.test_array)
        self.sorted(result)

    def testInsertionSort(self):
        result = insertion_sort(self.test_array)
        self.sorted(result)

    def testBubbleSort(self):
        result = bubble_sort(self.test_array)
        self.sorted(result)

    def testQuickSort(self):
        result = quick_sort(self.test_array)
        self.sorted(result)

    def testMergeSort(self):
        result = merge_sort(self.test_array)
        self.sorted(result)

    def testCountSort(self):
        result = counting_sort(self.test_array)
        self.sorted(result)

    def testRadixSort(self):
        result = radix_sort(self.test_array)
        self.sorted(result)


if __name__ == '__main__':
    unittest.main()
