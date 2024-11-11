import math


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        buyPrice = prices[0]
        for i in range(1, len(prices)):
            if buyPrice > prices[i]:
                buyPrice = prices[i]
            else:
                profit = max(profit, prices[i] - buyPrice)
        return profit


if __name__ == '__main__':
    sol = Solution()
    print(sol.maxProfit(prices=[7, 6, 4, 3, 1]))
