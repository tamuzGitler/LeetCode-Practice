class Solution(object):
    def zeroFilledSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = 0
        totalSubarrays = 0
        for num in nums:
            if num == 0:
                n += 1
            elif n > 0 :
                totalSubarrays +=  (n * (n + 1)) / 2
                n = 0
        totalSubarrays += (n * (n + 1)) / 2
        return totalSubarrays

if __name__ == '__main__':
    sol = Solution()
    nums = [1,3,0,0,2,0,0,4]
    nums = [0,0,0,2,0,0]

    print(sol.zeroFilledSubarray(nums))