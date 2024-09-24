class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        profit = 0
        s = prices[0]
        startI = 0
        prevMin = prices[0]
        for i in range(len(prices)):
            if prices[i] < s:
                s = prices[i]
                prevMin = s
            else:
                startI = i
                break
        j = startI + 1
        while j < len(prices):
            if prices[j] < prices[j - 1]:  # end of interval
                if prices[j - 1] - prevMin - fee < profit + prices[j - 1] - s - fee:
                    prevMin = s
                    profit = max(profit + prices[j - 1] - s - fee, 0)
                else:
                    profit = max(prices[j - 1] - prevMin - fee, 0)

                while j < len(prices) - 1 and prices[j] > prices[j + 1]:  # find min
                    j += 1
                s = prices[j]
                j += 1
            else:  # bigger
                if j + 1 >= len(prices):
                    profit = max(profit + prices[j] - s - fee, prices[j] - prevMin - fee, 0)
                    break
                j += 1
        return profit


if __name__ == '__main__':
    prices = [4, 5, 2, 4, 3, 3, 1, 2, 5, 4]

    fee = 1
    sol = Solution()
    print(sol.maxProfit(prices, fee))
