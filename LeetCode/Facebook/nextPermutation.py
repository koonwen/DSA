# Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
#
# If such an arrangement is not possible, it must rearrange it as the lowest possible order
# (i.e., sorted in ascending order).
#
# The replacement must be in place and use only constant extra memory.
from typing import List


def nextPermutation(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    i = len(nums) - 1
    while i > 0 and nums[i - 1] >= nums[i]:
        i -= 1
    i -= 1

    if i == -1:
        nums.reverse()
        return

    j = i + 1
    while j < len(nums) and nums[i] < nums[j]:
        j += 1
    j -= 1

    nums[i], nums[j] = nums[j], nums[i]

    i += 1
    j = len(nums)-1
    while i < j:
        nums[i], nums[j] = nums[j], nums[i]
        i += 1
        j -= 1


if __name__ == '__main__':
    nums = [1, 2, 3]
    nextPermutation(nums)
    assert ([1, 3, 2] == nums)
    nums = [3, 2, 1]
    nextPermutation(nums)
    assert ([1, 2, 3] == nums)
    nums = [1, 1, 5]
    nextPermutation(nums)
    assert ([1, 5, 1] == nums)
    nums = [1]
    nextPermutation(nums)
    assert ([1] == nums)
    nums = [2,3,1]
    nextPermutation(nums)
    assert([3,1,2] == nums)
    nums = [1,5,1]
    nextPermutation(nums)
    assert([5,1,1] == nums)
    nums = [5,1,1]
    nextPermutation(nums)
    assert ([1, 1, 5] == nums)
