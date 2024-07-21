class Solution(object):
    def garbageCollection(self, garbage, travel):
        """
        :type garbage: List[str]
        :type travel: List[int]
        :rtype: int
        """
        mTruck, pTruck, gTruck = 0, 0, 0
        trucks = {"P", "G", "M"}
        totalTravel = 0
        for i in range(len(travel), -1, -1):
            totalTravel += len(garbage[i])
            s = set()
            for t in trucks:
                if t in garbage[i]:
                    totalTravel += sum(travel[0:i])
                    s.add(t)
            trucks -= s
        return totalTravel


if __name__ == '__main__':
    garbage = ["MMM", "PGM", "GP"]
    travel = [3, 10]
    sol = Solution()
    print(sol.garbageCollection(garbage, travel))
