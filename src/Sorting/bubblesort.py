# Bubble Sort
from globalutils import timer

@timer
def bubble_sort(array:list) -> list:
    """Sorting Algorithm with O(n^2) runtime"""
    for current in range(len(array)-1):
        for index in range(current+1, len(array)):
            if array[index] < array[current]:
                array[index], array[current] = array[current], array[index]
    return array


if __name__ == "__main__":
    test_array = [23,31,24,324,3,32,2]
    result = bubble_sort(test_array)
    print(result)