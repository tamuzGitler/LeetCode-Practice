class Solution(object):
    def maximizeSum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        m = max(nums)
        maxSum = k * (m + (m + k - 1)) / 2
        return maxSum
