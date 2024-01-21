class Solution(object):
    def climbStairs(selfself,n):
        ans = [1,1]
        for i in range(2,n+1):
            ans.append(ans[i-1] + ans[i-2])
        return ans[n]


if __name__ == '__main__':
    sol = Solution()
    print(sol.climbStairs(1))
    print(sol.climbStairs(2))
    print(sol.climbStairs(3))
    print(sol.climbStairs(4))
    print(sol.climbStairs(5))
    print(sol.climbStairs(6))
