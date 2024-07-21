class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low = 0
        high = len(nums) - 1
        while(low <= high):
            mid = low + (high - low) // 2
            if((mid > 0 and nums[mid] < nums[mid-1]) and (mid < len(nums) - 1 and nums[mid] < nums[mid+1])):
                return nums[mid]
            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid - 1
        return nums[low]
if __name__ == '__main__':

   nums = [3,1,2]
   sol = Solution()
   print(sol.findMin(nums))