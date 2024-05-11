class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        ans = []
        q = []
        firstGreater = dict()
        for i, num in enumerate(nums2):
            while q and q[-1][1] < num:
                n = q.pop()[1]
                firstGreater[n] = num
            if num in nums1:  # find firstGreater only if num is in num1
                q.append((i, num))

        for i, num in enumerate(nums1):
            if num in firstGreater.keys():
                ans.append(firstGreater[num])
            else:
                ans.append(-1)
        return ans


if __name__ == '__main__':
    nums1 = [2, 4]
    nums2 = [1, 2, 3, 4]
    sol = Solution()
    print(sol.nextGreaterElement(nums1, nums2))
