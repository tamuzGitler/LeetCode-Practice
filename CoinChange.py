import math


class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        i = len(coins) - 1
        count = 0
        coins.sort()
        table = [0] * (amount + 1)
        for i in range(1,len(table)):
            if i in coins:
                table[i] = 1
            else:
                min_coins = math.inf
                for coin in coins:
                    if i - coin >= 0:
                        if table[i-coin] != -1:
                            min_coins = min(table[i-coin] + 1,min_coins)
                table[i] = min_coins if min_coins != math.inf else -1
        return table[-1]




if __name__ == '__main__':
    sol = Solution()
    coins = [1, 2, 5]
    amount = 11
    coins = [2]
    amount = 3
    print(sol.coinChange(coins, amount))
