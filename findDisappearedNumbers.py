class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        for i in range(len(nums)):
            val = abs(nums[i]) - 1

            nums[val] = -abs(val)
        missingValue = []
        for i in range(len(nums)):
            if nums[i] > 0:
                missingValue.append(i + 1)
        return missingValue

if __name__ == '__main__':
    nums = [4,3,2,7,8,2,3,1]
    # nums = [2,2]
    # nums = [1,4,4,4]

    sol = Solution()
    print(sol.findDisappearedNumbers(nums))