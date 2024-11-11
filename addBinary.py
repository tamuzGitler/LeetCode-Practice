class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        rest = 0
        binarySum = ""
        i, j = len(a) - 1, len(b) - 1
        while i >= 0 or j >= 0:
            curSum = rest
            curSum += int(a[i]) if i > -1 else 0
            curSum += int(b[j]) if j > -1 else 0
            binarySum = str(curSum % 2) + (binarySum)
            rest = curSum // 2
            i -= 1
            j -= 1
        if rest == 1:
            binarySum = str(rest) + binarySum
        return binarySum


if __name__ == '__main__':
    a = "11"
    b = "1"
    sol = Solution()
    print(sol.addBinary(a, b))
