from typing import List


def binary_search(nums: List[int], target: int) -> int:
    res1 = imp_binary_search(nums, target)
    res2 = rec_binary_search(nums, target)
    assert(res1 == res2)
    return res1


# Imperative solution
def imp_binary_search(nums: List[int], target: int) -> int:
    lo, hi = 0, len(nums)-1
    while lo < hi:
        mid = (lo + hi) >> 1
        if nums[mid] == target:
            return mid
        if nums[mid] > target:
            hi = mid - 1
        else:
            # Take note, integer division leads to round down
            # therefore we need to add one to 'lo' so that we prevent infinite loops
            lo = mid + 1
    return -1


# Recursive solution
def rec_binary_search(nums: List[int], target: int) -> int:
    def helper(lo, hi):
        if lo > hi:
            return -1
        mid = (lo + hi) >> 1
        if nums[mid] == target:
            return mid
        if nums[mid] > target:
            return helper(lo, mid - 1)
        else:
            return helper(mid + 1, hi)

    return helper(0, len(nums)-1)
