from collections import Counter


class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) > len(s2):
            return False
        return self.checkPermutation(s1, s2)

    def checkPermutation(self, shortString, longString):
        shortCounter = Counter(shortString)
        longCounter = Counter(longString[0: len(shortString)])
        for i in range(len(longString) - len(shortString) + 1):
            if i > 0:
                longCounter[longString[i + len(shortString) - 1]] = longCounter.setdefault(
                    longString[i + len(shortString) - 1], 0) + 1

            if longCounter == shortCounter:
                return True
            longCounter[longString[i]] -= 1
            if longCounter[longString[i]] == 0:
                del longCounter[longString[i]]
        return False


if __name__ == '__main__':
    s1 = "ab"
    s2 = "eidbaooo"
    sol = Solution()
    print(sol.checkInclusion(s1, s2))
