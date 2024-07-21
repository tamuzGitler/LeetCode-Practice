class Solution:
    def canCompleteCircuit(self, gas, cost):
        startInd = 0
        total = 0
        depth = 0
        for i in range(len(gas)):
            total += gas[i] - cost[i]
            if total < 0:
                depth += total
                total = 0
                startInd = i + 1
        if(depth + total < 0):
            return -1
        return startInd

if __name__ == '__main__':
    sol = Solution()
    gas = [2,3,4]
    cost = [3,4,3]
    gas = [1, 2, 3, 4, 5]
    cost = [3, 4, 5, 1, 2]
    print(sol.canCompleteCircuit(gas,cost))