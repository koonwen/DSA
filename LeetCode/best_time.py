def max_p(nums):
    l, r = 0, 1
    max_p = -1
    d = dict()

    while (r < len(nums)):
        diff = nums[r] - nums[l]
        if diff > 0:
            max_p = max(max_p, diff)
            d[max_p] = l, r
        else:
            l = r
        r += 1

    return max_p, d[max_p]


if __name__ == '__main__':
    test1 = [1, 2, 3, -14, -1, -5, 10]
    print(max_p(test1))