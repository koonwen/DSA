# Radix Sort

def get_number_column(number:int, column:int)->str:
    num_str = str(number)[::-1]
    result = '0' if len(num_str)-1 < column else num_str[column]
    return result


def radix_sort(array:list) -> list:
    """Sorting Algorithm with O(d+k) runtime"""
    maximum = max(array)
    columns = len(str(maximum))
    for col in range(columns):
        # sorted built in function is a stable sort which we are required to use here
        array = sorted(array, key=lambda num: get_number_column(num, col))
    return array


if __name__ == "__main__":
    test_array = [0, 1000, 4, 31, 410, 810, 998, 129, 129, 459, 559, 169, 179, 179, 189, 889]
    result = radix_sort(test_array)
    print(result)