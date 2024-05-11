class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        start = 0
        minLen = len(nums)
        curSum = 0
        for end, val in enumerate(nums):
            curSum += val
            while curSum >= target:
                minLen = min(minLen, (end - start) + 1)
                curSum -= nums[start]
                start += 1

        return minLen if minLen <= len(nums) else 0


if __name__ == '__main__':
    sol = Solution()
    target = 7
    nums = [2, 3, 1, 2, 4, 3]
    print(sol.minSubArrayLen(target, nums))
