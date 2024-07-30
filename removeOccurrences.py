class Solution(object):
    def removeOccurrences(self, s, part):
        """
        :type s: str
        :type part: str
        :rtype: str
        """
        while part in s:
            i = s.index(part)
            s = s[0:i] + s[i + len(part):]
        return s


if __name__ == '__main__':
    s = "daabcbaabcbc"
    part = "abc"
    sol = Solution()
    print(sol.removeOccurrences(s, part))
