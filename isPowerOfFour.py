class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if (n == 0):
            return False
        if (n == 1):
            return True
        if (n % 2 != 0):
            return False
        return self.isPowerOfFour(n / 2)


if __name__ == '__main__':
    sol = Solution()
    print(sol.isPowerOfFour())
