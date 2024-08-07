class Solution(object):
    def maxIceCream(self, costs, coins):
        """
        :type costs: List[int]
        :type coins: int
        :rtype: int
        """
        totalIcecreams = 0
        countingCosts = [0] * (max(costs) + 1)
        for cost in costs:
            countingCosts[cost] += 1

        for cost, cups in enumerate(countingCosts):
            if cost == 0:
                continue
            while (cups > 0):
                if coins - cost >= 0:
                    totalIcecreams += 1
                    cups -= 1
                    coins -= cost
                else:
                    break
        return totalIcecreams

        # costs.sort()
        # totalIcecreams = 0
        # for cost in costs:
        #     if coins - cost >= 0:
        #         totalIcecreams += 1
        #         coins -= cost
        #     else:
        #         break
        # return totalIcecreams


if __name__ == '__main__':
    sol = Solution()
    costs = [1, 3, 2, 4, 1]
    coins = 7
    print(sol.maxIceCream(costs, coins))
