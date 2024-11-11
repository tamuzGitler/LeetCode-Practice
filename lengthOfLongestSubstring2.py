class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxSub = 0
        start, end = 0, 0
        while (end < len(s)):
            if s[end] not in s[start:end]:
                end += 1
            else:
                maxSub = max(maxSub, end - start)
                start = start + s[start:end].index(s[end]) + 1
        maxSub = max(maxSub, end - start)

        return maxSub


if __name__ == '__main__':
    s = "abcabcbb"
    sol = Solution()
    print(sol.lengthOfLongestSubstring(s))
