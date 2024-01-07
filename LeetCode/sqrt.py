class Solution(object):
    # option 1
    def mySqrt1(self, x):
        """
        :type x: int
        :rtype: int
        """
        if not x:
            return x
        i = 1
        while ((i + 1) * (i + 1) <= x):
            i += 1
        return i

    # option 2 - binary search
    def mySqrt2(self, x):
        """
        :type x: int
        :rtype: int
        """
        if not x:
            return x
        l, r = 0, x
        while (l <= r):
            mid = l + (r-l) // 2
            if mid * mid <= x < (mid+1) * (mid+1):
                return mid
            elif mid * mid > x:
                r = mid - 1
            else:
                l = mid + 1


if __name__ == '__main__':
    x = 19
    sol = Solution()
    print(sol.mySqrt2(x))
