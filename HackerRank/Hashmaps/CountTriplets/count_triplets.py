from collections import Counter

# The frequency counter program makes use of two counters/dictionaries
# to keep track of the second element we expect in one counter and
# the third element we expect in another.
# The algorithm iterates over the list in one pass, looking at the element
# and adding a count to the element*common_ratio to the first dictionary.
# During each iteration, it also checks if the element is expected
# in the first dictionary (representing the second element in the
# triplet) and doubles the count for it's corresponding third value
# it expects in the third dictionary. This is an neccessary feature
# because if we encounter multiple same values, we then increase
# the number of times we can form a triplet by a factor of 2 each time.

# e.g. [1,1,1,2,2,4] ans = 6
# itr1 (1): expect_2nd = {2->1},             expect_3rd{},            cnt=0
# itr2 (1): expect_2nd = {2->2},             expect_3rd{},            cnt=0
# itr3 (1): expect_2nd = {2->3},             expect_3rd{},            cnt=0
# itr4 (2): expect_2nd = {2->3, 4->1},       expect_3rd{8->3},        cnt=0
# itr5 (2): expect_2nd = {2->4, 4->2},       expect_3rd{8->6},        cnt=0
# itr6 (4): expect_2nd = {2->4, 4->2, 8->1}, expect_3rd{8->6}         cnt=6


def count_triplets(arr, r):
    """
    Count the total number of triplets that can be formed as a sequence with the common ratio r
    :param arr:
    :param r:
    :return: total count
    """
    expect_2nd = Counter()
    expect_3rd = Counter()
    cnt = 0

    for num in arr:
        if num in expect_3rd:
            cnt += expect_3rd[num]

        if num in expect_2nd:
            expect_3rd[num * r] += expect_2nd[num]

        expect_2nd[num * r] += 1

    return cnt
