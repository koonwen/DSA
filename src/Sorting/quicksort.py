# Quick Sort

def quick_sort(array:list) -> list:
    """Sorting Algorithm with O(nlogn) runtime"""
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)


if __name__ == "__main__":
    test_array = [3,43,643,2,64536,3]
    result = quick_sort(test_array)
    print(result)
