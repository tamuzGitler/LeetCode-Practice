class Solution(object):
    def appendCharacters(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        i = 0
        for c in s:
            if i > len(t) - 1:
                break
            if c == t[i]:
                i += 1
        return len(t) - i


if __name__ == '__main__':
    s = "z"
    t = "abcde"
    sol = Solution()
    print(sol.appendCharacters(s, t))
