class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        rightSum = sum(nums) - nums[0]  # O(N)
        leftSum = 0
        pivot = 0
        while (leftSum != rightSum):
            leftSum += nums[pivot]
            pivot += 1
            rightSum -= nums[pivot]
            if pivot == len(nums) - 1:
                break

        return pivot if leftSum == rightSum else -1


if __name__ == '__main__':
    nums = [1, 7, 3, 6, 5, 6]
    nums = [1, 2, 3]
    # nums = [2, 1, -1]
    # nums = [-1, -1, 0, 1, 1, 0]

    sol = Solution()
    print(sol.pivotIndex(nums))
