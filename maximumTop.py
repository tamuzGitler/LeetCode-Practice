class Solution(object):
    def maximumTop(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if len(nums) == 1:
            if k % 2 == 0:
                return nums[0]
            return -1  # odd

        maxNum = 0
        for i in range(min(k - 1, len(nums))):
            maxNum = max(nums[i], maxNum)
        # last step, remove \ add
        if k + 1 <= len(nums):
            return max(maxNum, nums[k])
        else:
            return maxNum


if __name__ == '__main__':
    nums = [1, 2, 1000000000]

    k = 2
    sol = Solution()
    print(sol.maximumTop(nums, k))
