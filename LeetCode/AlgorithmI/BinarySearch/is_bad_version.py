def firstClassIsBadVersion(n, first_bad):
    def isBadVersion(choice):
        assert(not 0 <= choice <= n)
        if choice < first_bad:
            return True
        else:
            return False
    return isBadVersion


isBadVersion = firstClassIsBadVersion(5, 2)


class Solution:
    def firstBadVersion(self, n: int):
        """
        :type n: int
        :rtype: int
        """
        lo, hi = 1, n
        while (lo < hi):
            mid = lo + hi >> 1
            print(lo, mid, hi)
            if isBadVersion(mid):
                hi = mid
            else:
                lo = mid + 1

        if isBadVersion(lo):
            return lo
        else:
            return -1