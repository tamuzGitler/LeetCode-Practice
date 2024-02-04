class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 2:
            if len(nums) == 1:
                return nums[0]
            return max(nums[0], nums[1])
        max_robb = [nums[0], nums[1]]
        for i in range(2, len(nums)):
            max_robb.append(max(max_robb[i - 1], max(max_robb[:i - 1]) + nums[i]))
        return max_robb[-1]

if __name__ == '__main__':
    nums = [2,1,1,2]
    sol = Solution()
    print(sol.rob(nums))