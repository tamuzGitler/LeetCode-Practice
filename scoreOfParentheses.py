class Solution(object):
    def scoreOfParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        score = 0

        for c in s:
            if c == "(":
                stack.append(score)
                score = 0
            else:
                score = stack.pop() + max(score * 2, 1)
                # A -> stack.pop()
        return score


if __name__ == '__main__':
    sol = Solution()
    s = "()()"
    print(sol.scoreOfParentheses(s))
