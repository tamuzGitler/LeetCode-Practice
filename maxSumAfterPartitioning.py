class Solution(object):
    def maxSumAfterPartitioning(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        dp = [arr[0]]
        for i in range(1, len(arr)):
            maxPartition = 0
            for j in range(max(0, i - k + 1), i + 1):
                curPartition = max(arr[j:min(i + 1, len(arr))]) * min(i - j + 1, k)
                if j - 1 >= 0:
                    curPartition += dp[j - 1]
                if curPartition > maxPartition:
                    maxPartition = curPartition
            dp.append(maxPartition)
        return dp[-1]


if __name__ == '__main__':
    # arr = [1, 4, 1, 5, 7, 3, 6, 1, 9, 9, 3]
    k = 1
    arr = [7, 2]
    sol = Solution()
    print(sol.maxSumAfterPartitioning(arr, k))
    # print(sum([15, 15, 15, 9, 10, 10, 10]))
