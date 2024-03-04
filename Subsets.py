
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        subset = []
        self.dfs(0, nums, res, subset)
        return res

    def dfs(self, i, nums, res, subset):
        if i >= len(nums):
            res.append(subset.copy())
            return
        # add num
        subset.append(nums[i])
        self.dfs(i + 1, nums, res, subset)
        subset.pop()
        self.dfs(i + 1, nums, res, subset)


if __name__ == '__main__':
    nums = [1, 2, 3]
    sol = Solution()
    print(sol.subsets(nums))
