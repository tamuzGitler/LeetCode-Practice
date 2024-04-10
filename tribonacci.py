class Solution:
    def tribonacci(self, n: int) -> int:
        ans = [0, 1, 1]
        if n < 3:
            return ans[n]
        for i in range(3, n + 1):
            ans.append(sum(ans[i - 3: i]))
        return ans[n]


if __name__ == '__main__':
    sol = Solution()
    print(sol.tribonacci(4))
