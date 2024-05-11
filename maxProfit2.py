class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        profit = 0
        prevStockPrice = prices[0]
        for i in range(1, len(prices)):
            if prices[i] > prevStockPrice:
                profit += prices[i] - prevStockPrice
            prevStockPrice = prices[i]
        return profit


if __name__ == '__main__':
    prices = [7, 1, 5, 3, 6, 4]
    prices = [1, 7, 4, 2, 11]
    # prices = [6, 1, 3, 2, 4, 7]

    sol = Solution()
    print(sol.maxProfit(prices))
