import math


class Solution(object):
    def minPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        s, e = 1, len(nums) - 2
        minPairs = nums[s - 1] + nums[e + 1]
        while (s < e):
            minPairs = max(minPairs, nums[s] + nums[e])
            s += 1
            e -= 1
        return minPairs
