# Counting sort
from globalutils import timer


@timer
def counting_sort(array: list) -> list:
    lo = min(array)
    hi = max(array)
    offset = 0 if lo > 0 else -lo
    freq_array = [0] * (hi + offset + 1)
    for elem in array:
        freq_array[elem + offset] += 1

    hist_array = [freq_array[0]]
    for index in range(1, len(freq_array)):
        hist_array.append(hist_array[index - 1] + freq_array[index])

    result = [0] * len(array)
    cnt = len(array) - 1
    for index in range(len(hist_array) - 1, -1, -1):
        for i in range(freq_array[index]):
            result[cnt] = index
            cnt -= 1
    return result


if __name__ == "__main__":
    test_array = [3, 4, 6, 2, 3, 2, 5]
    result = counting_sort(test_array)
    print(result)
