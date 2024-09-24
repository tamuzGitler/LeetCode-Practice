class Solution(object):
    def isAcronym(self, words, s):
        """
        :type words: List[str]
        :type s: str
        :rtype: bool
        """
        if len(s) != len(words):
            return False
        for i, word in enumerate(words):
            if word[0] != s[i]:
                return False
        return True


if __name__ == '__main__':
    words = ["alice", "bob", "charlie"]
    s = "abc"
    sol = Solution()
    print(sol.isAcronym(words, s))
