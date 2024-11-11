class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prev = 0
        for num in nums:
            prev = prev | num
        return prev
