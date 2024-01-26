class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        uniqueNums1 = set(nums1)
        uniqueNums2 = set(nums2)
        return [list(uniqueNums1 - uniqueNums2), list(uniqueNums2 - uniqueNums1)]


if __name__ == '__main__':
    sol = Solution()
    print(sol.findDifference(nums1=[1, 2, 3], nums2=[2, 4, 6]))
