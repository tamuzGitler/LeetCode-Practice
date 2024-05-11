class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not len(s):
            return 0
        start, end = 0, 0
        subLen = 1
        while (end < len(s)):
            # yes
            if end == len(s) - 1 or s[end + 1] == s[start]:
                subLen = max((end - start) + 1, subLen)
                start += 1
            elif s[end + 1] in s[start:end + 1]:
                subLen = max((end - start) + 1, subLen)
                start, end = s[start:end + 1].index(s[end + 1]) + 1 + start, end
            # no
            end += 1

        return subLen


if __name__ == '__main__':
    sol = Solution()
    s = "abcabcbb"
    s = "ggububgvfk"
    # s = "pwwkew"
    # s = 'bbbb'
    # s = 'ab'
    print(sol.lengthOfLongestSubstring(s))
