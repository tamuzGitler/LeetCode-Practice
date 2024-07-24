class Solution(object):
    def pivotArray(self, nums, pivot):
        """
        :type nums: List[int]
        :type pivot: int
        :rtype: List[int]
        """
        smallers = []
        greaters = []

        for i in range(len(nums)):
            num = nums[i]
            if num < pivot:
                smallers.append(num)
            elif num > pivot:
                greaters.append(num)

        for i in range(len(smallers)):
            nums[i] = smallers[i]

        for i in range(len(smallers), len(nums) - len(greaters)):
            nums[i] = pivot

        for i in range(0, len(greaters)):
            nums[len(nums) - len(greaters) + i] = greaters[i]

        return nums


if __name__ == '__main__':
    nums = [9, 12, 5, 10, 14, 3, 10]

    sol = Solution()
    print(sol.pivotArray(nums, 10))
