class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        minSoFar, maxSoFar, totalMax = nums[0], nums[0], max(nums)
        for i in range(1, len(nums)):
            if nums[i] == 0:
                minSoFar, maxSoFar = 1, 1
            else:
                tempMin = minSoFar
                minSoFar = min(nums[i] * minSoFar, maxSoFar * nums[i], nums[i])
                maxSoFar = max(nums[i] * tempMin, maxSoFar * nums[i], nums[i])
                totalMax = max(totalMax, maxSoFar)
        return totalMax


if __name__ == '__main__':
    nums = [-2, 0, -1]
    sol = Solution()
    print(sol.maxProduct(nums))
