from functools import reduce


class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        convertedNum1 = self.convertToInt(num1)
        convertedNum2 = self.convertToInt(num2)
        prod = convertedNum1 * convertedNum2
        if prod == 0:
            return '0'
        prodS = self.convertToString(prod)
        return prodS

    def convertToInt(self, num):
        mult = 10
        number = 0
        for i in range(len(num)):
            number = number * mult + int(num[i])
        return number

    def convertToString(self, num):
        s = ''
        while (num > 0):
            s = str(num % 10) + s
            num //= 10
        return s


if __name__ == '__main__':
    num1 = '30'
    num2 = '12'
    sol = Solution()
    print(sol.multiply(num1, num2))
