import numpy
class Solution(object):
    def arraySign(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        posFlag = 1
        for val in nums:
            if val == 0:
                return 0
            if val < 0:
                posFlag *= -1
        return posFlag

if __name__ == '__main__':
    nums = [-1, -2, -3, -4, 3, 2, 1]
    sol = Solution()
    print(sol.arraySign(nums))