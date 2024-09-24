class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # dp = [[0] * n] * m
        dp = [[0 for _ in range(n)] for _ in range(m)]

        for col in range(n):
            dp[m - 1][col] = 1
        for row in range(m):
            dp[row][n - 1] = 1
        for row in range(m - 2, -1, -1):
            for col in range(n - 2, -1, -1):
                dp[row][col] = dp[row + 1][col] + dp[row][col + 1]
        return dp[0][0]


if __name__ == '__main__':
    m, n = 1, 1
    sol = Solution()
    print(sol.uniquePaths(m, n))
