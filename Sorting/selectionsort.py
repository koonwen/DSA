# Selection Sort

def selection_sort(array:list) -> list:
    result = []
    for i in range(len(array)):
        array_min = min(array)
        result.append(array_min)
        array.remove(array_min)
    return result


if __name__ == "__main__":
    test_array = [32,532,2345,342,31,3,42]
    result = selection_sort(test_array)
    print(result)