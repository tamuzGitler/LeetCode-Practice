class Solution(object):
    def canAliceWin(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        singleDig = 0
        doubleDig = 0
        for num in nums:
            if num < 10:
                singleDig += num
            else:
                doubleDig += num
        return singleDig != doubleDig
