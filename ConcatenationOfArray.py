class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = [0] * len(nums) * 2
        for i,num in enumerate(nums):
            ans[i] = num
            ans[i+len(nums)] = num
        return ans

if __name__ == '__main__':
    sol = Solution()
    ans = sol.getConcatenation([1,2,3])
    print((ans))