from collections import Counter


class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = Counter(nums)
        maxHS = 0

        for key in count.keys():
            if key + 1 in count.keys():
                maxHS = max(maxHS, count[key] + count[key + 1])
        return maxHS


if __name__ == '__main__':
    nums = [1, 3, 2, 2, 3, 5, 7]
    sol = Solution()
    print(sol.findLHS(nums))
