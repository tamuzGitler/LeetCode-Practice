class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        missingSum = (len(nums) + 1) * (2 * 0 + len(nums)) / 2
        sumOfNum = sum(nums)
        return missingSum - sumOfNum


if __name__ == '__main__':
    sol = Solution()
    nums = [1, 3]
    print(sol.missingNumber(nums))
    nums = [1, 3, 4, 2, 5]
    print(sol.missingNumber(nums))
