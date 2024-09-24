class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeros = nums.count(0)
        zeroLocation = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[zeroLocation] = nums[i]
                zeroLocation += 1
        for i in range(len(nums) - 1, len(nums) - 1 - zeros, -1):
            nums[i] = 0


if __name__ == '__main__':
    nums = [0, 1, 0, 3, 12]
    sol = Solution()
    sol.moveZeroes(nums)
    print(nums)
