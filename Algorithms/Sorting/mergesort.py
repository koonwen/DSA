# Mergesort
from globalutils import timer


def divides(l, r):
	"""finds the midpoint in the array and handles the case of dividing odd numbers
	because of floor division"""
	total = l+r
	result = (total//2 + 1) if total % 2 else total // 2
	return result


def merge(subarr1, subarr2):
	"""Combines two arrays returning a combined sorted array"""
	result = []
	while not (subarr1 == [] and subarr2 == []):
		if not subarr1:
			result.extend(subarr2)
			subarr2.clear()
		elif not subarr2:
			result.extend(subarr1)
			subarr1.clear()
		else:
			if subarr1[0] < subarr2[0]:
				result.append(subarr1.pop(0))
			else:
				result.append(subarr2.pop(0))
	return result

@timer
def merge_sort(array, left=0, right=None):
	"""Sorting algorithm with O(nlogn) runtime"""
	def merge_sort_rec(array, left=0, right=None):
		if right is None:
			right = len(array)-1

		if left > right:
			return []
		if left == right:
			return [array[left]]

		mid = divides(left, right)
		l = merge_sort_rec(array, left, mid-1)
		r = merge_sort_rec(array, mid, right)
		result = merge(l, r)

		return result

	return merge_sort_rec(array, left, right)