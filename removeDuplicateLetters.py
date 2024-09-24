class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        lexS = ""
        for i in range(len(s) - 1, -1, -1):
            c = s[i]
            if s[i] not in lexS:
                lexS = s[i] + lexS
            elif s[i] < lexS[0]:
                lexS = lexS.replace(s[i], '')
                lexS = s[i] + lexS
        return lexS


if __name__ == '__main__':
    s = "abacb"
    sol = Solution()
    print(sol.removeDuplicateLetters(s))
    b, c, a,
