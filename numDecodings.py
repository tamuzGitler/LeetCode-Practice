class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        waysToDecode = [1, 1]
        if not s or s[0] == '0':
            return 0
        for i in range(1, len(s)):
            c = s[i]
            ways = 0
            if s[i] == '0':
                twoDigits = int(s[i - 1:i + 1])

                if s[i - 1] != '0' and twoDigits >= 10 and twoDigits <= 26:
                    ways += waysToDecode[- 2]
                else:
                    return 0
            else:
                # seperate
                ways += waysToDecode[-1]
                twoDigits = int(s[i - 1:i + 1])
                if twoDigits >= 10 and twoDigits <= 26:
                    ways += waysToDecode[-2]
            waysToDecode.append(ways)
        return waysToDecode[-1]


if __name__ == '__main__':
    sol = Solution()
    s = "12120"
    print(sol.numDecodings(s))
