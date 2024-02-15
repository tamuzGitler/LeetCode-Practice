class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeros = nums.count(0)
        p = 0
        for i in range(len(nums)):
            if nums[i] != 0:

                nums[p] = nums[i]
                p += 1
        for j in range(zeros):
            nums[len(nums) - 1 - j] = 0


if __name__ == '__main__':
    nums = [0, 1, 0, 3, 12]
    sol = Solution()
    sol.moveZeroes(nums)
    print(nums)