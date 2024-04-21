class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if sum(gas) < sum(cost):
            return -1

        totalCost = 0
        j = 0
        for i in range(len(gas)):
            totalCost += gas[i] - cost[i]
            if totalCost < 0:
                totalCost = 0
                j = i + 1
        return j


if __name__ == '__main__':
    sol = Solution()
    gas = [1, 2, 3, 4, 5]
    cost = [3, 4, 5, 1, 2]
    print(sol.canCompleteCircuit(gas, cost))
