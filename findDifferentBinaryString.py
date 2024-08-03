class Solution(object):
    def findDifferentBinaryString(self, nums):
        """
        :type nums: List[str]
        :rtype: str
        """
        self.ans = ''
        self.createStrings(nums, '')
        return self.ans

    def createStrings(self, nums, s):
        if (len(s) == len(nums)):
            if s not in nums:
                self.ans = s
            return

        self.createStrings(nums, s + '0')
        self.createStrings(nums, s + '1')
