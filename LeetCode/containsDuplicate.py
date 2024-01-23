class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        apperances = set() # hashset
        for num in nums:
            if num in apperances:
                return True
            else:
                apperances.add(num)
        return False
