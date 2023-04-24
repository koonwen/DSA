# InsertionSort
from globalutils import timer


def insert(elem, array):
	"""insert elem into array in ascending order"""
	if array is []:
		return [elem]
	for index, value in array:
		if elem < value:
			array.insert(index, elem)
	return array

@timer
def insertion_sort(array):
	"""sorting algorithm with O(n^2) runtime"""
	result = []
	for elem in array:
		insert(elem, result)
	return result
