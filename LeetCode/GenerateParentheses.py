class Solution(object):
    def generateParenthesis(self,n):
        if n == 0:
            return []

        # Dynamic programming table to store results of subproblems
        dp = [[] for _ in range(n + 1)]
        dp[0] = [""]

        for i in range(1, n + 1):
            for j in range(i):
                # Iterate over all combinations of parentheses for dp[j]
                for x in dp[j]:
                    # Iterate over all combinations of parentheses for dp[i - j - 1]
                    for y in dp[i - j - 1]:
                        # Combine the three parts to form a new combination and add it to dp[i]
                        dp[i].append("(" + x + ")" + y)
        return dp[n]
if __name__ == '__main__':
    sol = Solution()
    # print(sol.generateParenthesis(1))
    # print(sol.generateParenthesis(2))
    print(sol.generateParenthesis(3))
    print(sol.generateParenthesis(4))
