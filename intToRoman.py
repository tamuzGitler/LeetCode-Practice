romans = [
    ["I", 1],
    ["IV", 4],
    ["V", 5],
    ["IX", 9],
    ["X", 10],
    ["XL", 40],
    ["L", 50],
    ["XC", 90],
    ["C", 100],
    ["CD", 400],
    ["D", 500],
    ["CM", 900],
    ["M", 1000]
]


class Solution(object):

    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        romanNumeral = ''
        for symbol, val in reversed(romans):
            if num // val > 0:
                count = num // val  # number of letters needed
                romanNumeral += symbol * count
                num -= val * count
        return romanNumeral


if __name__ == '__main__':
    sol = Solution()
    print(sol.intToRoman(1940))
