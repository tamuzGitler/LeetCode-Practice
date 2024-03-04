class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res =[]
        if len(nums) == 1:
            return [nums[:]]
        for i in range(len(nums)):
            n = nums.pop(0)
            permuts = self.permute(nums)
            for permut in permuts:
                permut.append(n)
            res.extend(permuts)
            nums.append(n)
        return res



if __name__ == '__main__':
    sol = Solution()
    nums = [1,2,3]
    print(sol.permute(nums))

