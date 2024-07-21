class Solution(object):
    def minSteps(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        steps = 0
        for c in set(t):
            steps += max(t.count(c) - s.count(c), 0)
        return steps


if __name__ == '__main__':
    s = "aba"
    t = "bba"
    sol = Solution()
    print(sol.minSteps(s, t))
