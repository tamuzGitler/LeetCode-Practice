import sys


class Solution(object):
    def minimumDeletions(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        count = 0
        for c in s:
            if c == 'b':
                stack.append('b')
            elif stack and c == 'a':
                stack.pop()
                count += 1
        return count


if __name__ == '__main__':
    s = "ababaaaabbbbbaaababbbbbbaaabbaababbabbbbaabbbbaabbabbabaabbbababaa"

    sol = Solution()
    print(sol.minimumDeletions(s))
