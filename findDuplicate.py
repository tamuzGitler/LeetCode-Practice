class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow = 0
        fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        secondSlow = 0
        while(secondSlow != slow):
            secondSlow = nums[secondSlow]
            slow = nums[slow]
        return slow

if __name__ == '__main__':
    nums = [1,3,4,2,2]
    # nums = [3,1,3,4,2]
    # nums = [3,3,3,3,3]
    sol = Solution()
    print(sol.findDuplicate(nums))
