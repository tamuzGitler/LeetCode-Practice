class Solution(object):
    # O(N^2) solution
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        maxSub = ""
        for i in range(len(s)):
            l, r = i, i
            # odd
            while (l >= 0 and r < len(s) and s[l] == s[r]):
                maxSub = s[l:r + 1] if (r - l + 1) > len(maxSub) else maxSub
                l -= 1
                r += 1
            # even
            l, r = i, i + 1
            while (l >= 0 and r < len(s) and s[l] == s[r]):
                maxSub = s[l:r + 1] if (r - l + 1) > len(maxSub) else maxSub
                l -= 1
                r += 1

        return maxSub


if __name__ == '__main__':
    sol = Solution()
    s = "ccd"

    print(sol.longestPalindrome(s))
