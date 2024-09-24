class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if len(s) <= 3:
            return s
        maxVowels = 0
        vowels = {'a', 'e', 'i', 'o', 'u'}
        curSub = s[:k]

        for c in curSub:
            if c in vowels:
                maxVowels += 1
        vowelsCount = maxVowels
        for i in range(1, len(s) - k + 1):
            if curSub[0] in vowels:
                vowelsCount -= 1

            curSub = curSub[1:] + s[i + k - 1]
            if s[i + k - 1] in vowels:
                vowelsCount += 1
            if vowelsCount == k:
                return vowelsCount
            elif vowelsCount > maxVowels:
                maxVowels = vowelsCount
        return maxVowels


if __name__ == '__main__':
    s = "weallloveyou"
    k = 7
    sol = Solution()
    print(sol.maxVowels(s, k))
