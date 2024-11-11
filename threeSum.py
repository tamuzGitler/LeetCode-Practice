class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        ans = []
        i = 0
        while (i < len(nums) - 2):
            m, e = i + 1, len(nums) - 1
            while (m < e):
                if (nums[i] + nums[m] + nums[e] == 0):
                    ans.append([nums[i], nums[m], nums[e]])

                    while (m < e and nums[e] == nums[e - 1]):
                        e -= 1
                    while (m < e and nums[m] == nums[m + 1]):
                        m += 1
                    m += 1
                    e -= 1
                elif (nums[i] + nums[m] + nums[e] > 0):
                    e -= 1
                else:
                    m += 1
            while (i < len(nums) - 2 and nums[i] == nums[i + 1]):
                i += 1
            i += 1
        return ans


if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, -4]
    sol = Solution()
    print(sol.threeSum(nums))
