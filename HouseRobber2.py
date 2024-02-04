class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        arr1, arr2 = nums[:len(nums) - 1], nums[1:]
        if len(nums) <= 3:
            return max(self.checkSmallArr(arr2),self.checkSmallArr(arr1))
        return max(self.helper(arr1), self.helper(arr2))
    def checkSmallArr(self,nums):
        if len(nums) <= 2:
            if len(nums) == 1:
                return nums[0]
            return max(nums[0], nums[1])
    def helper(self, nums):

        max_robb = [nums[0], nums[1]]
        for i in range(2, len(nums)):
            max_robb.append(max(max_robb[i - 1], max(max_robb[:i - 1]) + nums[i]))
        return max_robb[-1]
if __name__ == '__main__':
    nums1 = [2,3,2]
    nums2 = [1,2,3,1]
    nums3 = [1,2,3]
    nums4= [1,2,1,1]
    nums5= [200,3,140,20,10]
    nums6 = [4,1,2]



    sol = Solution()
    # print(sol.rob(nums1))
    # print(sol.rob(nums2))
    # print(sol.rob(nums3))
    # print(sol.rob(nums4))
    # print(sol.rob(nums5))
    print(sol.rob(nums6))