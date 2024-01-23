class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        ans = [0]
        for i in range(1, n + 1):
            if i % 2 == 1:
                ans.append(ans[i-1] + 1)
            else:
                ans.append(ans[i//2])
        return ans
if __name__ == '__main__':
    sol = Solution()
    print(sol.countBits(1))
    print(sol.countBits(2))
    print(sol.countBits(3))
    print(sol.countBits(4))
    print(sol.countBits(5))
    print(sol.countBits(6))
    print(sol.countBits(7))