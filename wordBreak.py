class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        can_build = [None] * (len(s) + 1)
        can_build[-1] = True
        return self.helper(s, wordDict, can_build, 0)

    def helper(self, s, wordDict, can_build, i):
        for word in wordDict:
            if len(word) <= len(s) - i:
                if word == s[i:len(word) + i]:
                    if can_build[i + len(word)]:
                        return True
                    elif can_build[len(word) + i] == None:
                        ans = self.helper(s, wordDict, can_build, i + len(word))
                        if ans:
                            return True

        can_build[i] = False
        return False


if __name__ == '__main__':
    s = "leetcode"
    wordDict = ["leet", "code"]
    s = "applepenapple"
    wordDict = ["apple", "pen"]
    s = "catscatdog"

    wordDict = ["cat", "cats", "dog"]

    # s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    # wordDict = ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"]

    sol = Solution()
    print(sol.wordBreak(s, wordDict))
