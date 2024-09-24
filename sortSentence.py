class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = (s.split(' '))
        sortedS = [''] * len(s)
        for word in s:
            sortedS[int(word[-1]) - 1] = word[:-1]
        return " ".join(str(x) for x in sortedS)


if __name__ == '__main__':
    s = "is2 sentence4 This1 a3"
    sol = Solution()
    print(sol.sortSentence(s))
