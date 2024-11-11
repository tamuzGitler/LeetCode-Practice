class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.permutations = []
        stack = []
        self.backTrack(nums, stack)
        return self.permutations

    def backTrack(self, nums, stack):
        if not nums:
            self.permutations.append(stack[:])
            return
        i = 0
        while (i < len(nums)):
            stack.append(nums[0])
            removedVal = nums.pop(0)
            self.backTrack(nums, stack)
            stack.pop()
            nums.append(removedVal)
            i += 1


if __name__ == '__main__':
    nums = [1, 2, 3]
    sol = Solution()
    print(sol.permute(nums))
