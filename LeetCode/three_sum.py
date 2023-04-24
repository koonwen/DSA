from typing import List


def two_sum(nums: List[int], target) -> List[List[int]]:
    d = {}
    res = []
    for i, v in enumerate(nums):
        if v in d:
            res.append([d[v], v])
        d[target - v] = v
    return res

def three_sum(nums: List[int]) -> List[List[int]]:
    nums.sort()
    res = list()

    for i, v in enumerate(nums):
        if v > 0:
            break

        if i > 0 and v == nums[i-1]:
            continue

        l = i+1
        r = len(nums)-1

        while l < r:
            total = v + nums[l] + nums[r]
            if total > 0:
                r -= 1
            elif total < 0:
                l += 1
            else:
                res.append([v, nums[l], nums[r]])
                l += 1
                while l < r and nums[l] == nums[l - 1]:
                    l += 1
    return res


if __name__ == '__main__':
    test1 = [1, -5, 4, 1, 4]
    test2 = []
    test3 = [1,1,1,1,1,1,1,1,1,1,1,1]
    print(three_sum(test3))
