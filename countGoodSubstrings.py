class Solution(object):
    def countGoodSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        goodSubString = 0

        for i in range(0,len(s)-2):
            if 3 == len(set(s[i:i+3])):
                goodSubString += 1
        return goodSubString
if __name__ == '__main__':
    s = "abcdd"
    sol = Solution()
    print(sol.countGoodSubstrings(s))