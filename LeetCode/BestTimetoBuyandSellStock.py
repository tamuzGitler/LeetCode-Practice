class Solution(object):

    # def maxProfit(self, prices):
    #     """
    #     :type prices: List[int]
    #     :rtype: int
    #     """
    #     max_profit = 0
    #     min_index = len(prices)
    #     while(min_index != 0):
    #         min_index = prices.index(min(prices[:min_index]))
    #         max_index = prices.index(max(prices[min_index:]))
    #
    #         if max_profit < prices[max_index] - prices[min_index]:
    #             max_profit = prices[max_index] - prices[min_index]
    #     return max_profit

    # solution using pointers to buy and sell stock, O(N) time, O(1) space
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy_pointer, sell_pointer = 0,1
        if len(prices) == 1:
            return 0
        max_profit = 0
        while(sell_pointer < len(prices)):
            if prices[sell_pointer] < prices[buy_pointer]:
                buy_pointer = sell_pointer
                sell_pointer += 1
            else:
                max_profit = max(prices[sell_pointer] - prices[buy_pointer],max_profit)
                sell_pointer += 1
        return max_profit


if __name__ == '__main__':
    sol = Solution()
    prices = [7, 1, 5, 3, 6, 4]
    print(sol.maxProfit(prices))
    prices = [7, 6, 4, 3, 1,0]
    print(sol.maxProfit(prices))
    prices = [2,4,1]
    print(sol.maxProfit(prices))
    prices = [1,2]
    print(sol.maxProfit(prices))
    prices = [3,2,6,5,0,3]
    print(sol.maxProfit(prices))

