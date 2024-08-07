class Solution(object):
    def countVowelStrings(self, n):
        """
        :type n: int
        :rtype: int
        """

        a, e, i, o, u = 1, 1, 1, 1, 1
        for t in range(1, n):
            a, e, i, o = a + e + i + o + u, e + i + o + u, i + o + u, o + u
        return a + e + i + o + u


if __name__ == '__main__':
    n = 33
    sol = Solution()
    print(sol.countVowelStrings(n))
