class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        def bfs(left, right, s):
            if len(s) == 2 * n:
                res.append(s)
                return
            if left < n:
                bfs(left + 1, right, s + "(")
            if left > right:
                bfs(left, right + 1, s + ")")

        res = []
        s = ""
        bfs(0, 0, s)
        return res


if __name__ == '__main__':
    n = 3
    sol = Solution()
    print(sol.generateParenthesis(n))
