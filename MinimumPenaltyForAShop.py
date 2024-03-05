class Solution(object):
    def bestClosingTime(self, customers):
        """
        :type customers: str
        :rtype: int
        """
        curPenalty = customers.count("Y") 
        p = curPenalty
        minPenalty = curPenalty
        minHour = 0
        for i in range(len(customers)):
            if customers[i] == "Y":
                curPenalty -= 1
            else:
                curPenalty +=1
            if curPenalty < minPenalty:
                minPenalty = curPenalty
                minHour = i + 1
        # edge case!
        if customers.count("N") < minPenalty:
            return len(customers)
        return minHour
    # Time limit solution
    # def bestClosingTimeTime(self, customers):
    #     """
    #     :type customers: str
    #     :rtype: int
    #     """
    #     curPenalty = customers.count("Y")
    #     minPenalty = curPenalty
    #     minHour = 0
    #     for i in range(1,len(customers)+1):
    #         curPenalty = customers[:i].count("N") + customers[i:].count("Y")
    #         if curPenalty < minPenalty:
    #             minPenalty = curPenalty
    #             minHour = i
    #     return minHour
if __name__ == '__main__':
    sol = Solution()
    customers = "YYNY"
    print(sol.bestClosingTime(customers))