class Solution(object):
    def maxResult(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ans = [nums[0]]
        maxVal = nums[0]
        for i in range(1, len(nums)):
            ans.append(nums[i] + max(ans[max(0, len(ans) - k):]))
        return ans[-1]


if __name__ == '__main__':
    nums = [1, -1, -2, 4, -7, 3]
    k = 2
    sol = Solution()
    print(sol.maxResult(nums, k))
