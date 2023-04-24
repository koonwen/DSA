# The intuition behind this problem is that you want to find the maximum of
# a contiguous block unlike the max_profit, where you want to find the greatest
# difference. Hence to solve this problem, you want to keep the max_so_far as
# well as the current_sum. We update the current_sum to be 0 as soon as we encounter
# it to be zero.

def max_subarray(nums):
    curSum = 0
    maxSub = -1

    for i in nums:
        if curSum < 0:
            curSum = 0
        curSum += i
        maxSub = max(curSum, maxSub)

    return maxSub


def max_sub_p(nums):
    l, r = 0, 0
    curSum = 0
    max_sub = -1
    d = dict()

    while r < len(nums):
        if curSum < 0:
            curSum = 0
            l = r
        curSum += nums[r]
        r += 1
        if curSum > max_sub:
            d[curSum] = l, r
            max_sub = curSum

    return max_sub, d[max_sub]


if __name__ == '__main__':
    test1 = [1, 2, 3, -14, -1, -5, 10]
    test2 = []
    print(max_sub_p(test1))
