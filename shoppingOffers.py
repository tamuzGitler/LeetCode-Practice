class Solution(object):
    def shoppingOffers(self, price, special, needs):
        """
        :type price: List[int]
        :type special: List[List[int]]
        :type needs: List[int]
        :rtype: int
        """
        return self.dfs(price, special, needs, {})

    def dfs(self, price, special, needs, memo):
        print(memo)
        if tuple(needs) in memo:
            return memo[tuple(needs)]
        cost = 0
        for i, need in enumerate(needs):
            cost += need * price[i]

        for offer in special:
            newNeeds = []
            legalOffer = True
            for i in range(len(needs)):
                newNeeds.append(needs[i] - offer[i])
                if needs[i] - offer[i] < 0:
                    legalOffer = False
            if legalOffer:
                cost = min(cost, offer[-1] + self.dfs(price, special, newNeeds, memo))
                print(cost)
        memo[tuple(needs)] = cost
        return cost


if __name__ == '__main__':
    price = [2, 5]
    special = [[3, 0, 5], [1, 2, 10]]
    needs = [3, 2]
    sol = Solution()
    print(sol.shoppingOffers(price, special, needs))
