class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        sheerit = 1
        for i in range(len(digits) - 1, -1, -1):
            digits[i] = digits[i] + sheerit
            if digits[i] == 10:
                digits[i] = 0
                sheerit = 1
            else:
                sheerit = 0
        if sheerit == 1:
            digits.insert(0,1)
        return digits

if __name__ == '__main__':
    digits = [1,2,3]
    digits = [4, 3, 2, 1]
    digits = [9]
    digits = [9,9,9]
    sol = Solution()
    sol.plusOne(digits)
    print(digits)