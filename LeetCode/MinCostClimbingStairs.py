class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        min_payment = [cost[0], cost[1]]
        i = 2
        while(i < len(cost)):
            min_payment.append(min(min_payment[i-2] + cost[i], min_payment[i-1] + cost[i] ))
            i+=1
        return min(min_payment[-1], min_payment[-2])

if __name__ == '__main__':
    sol = Solution()
    # print(sol.minCostClimbingStairs([10,15,20]))
    # print(sol.minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]))
    print(sol.minCostClimbingStairs([0,1,2,2]))
