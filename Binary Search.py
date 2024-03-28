class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start, end = 0, len(nums)
        while (start < end):
            mid = (end - start) // 2 + start
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid
        return -1


if __name__ == '__main__':
    nums = [-1, 0, 3, 5, 9, 12]
    target = 9

    nums = [-1, 0, 5]
    target = -1
    # nums = [-1,0,3,5,9,12]
    # target = 2
    sol = Solution()
    print(sol.search(nums, target))
