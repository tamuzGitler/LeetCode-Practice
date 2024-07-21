class Solution(object):
    def groupThePeople(self, groupSizes):
        groupMap = dict()
        groups = []
        for i, demand in enumerate(groupSizes):
            groupMap.setdefault(demand, []).append(i)
        for demand in groupMap.keys():
            ppl = groupMap[demand]
            curGroup = []
            for i in range(len(ppl)):
                curGroup.append(ppl[i])
                if len(curGroup) == demand:
                    groups.append(curGroup)
                    curGroup = []
        return groups

    # nlogn
    def groupThePeople2(self, groupSizes):
        """
        :type groupSizes: List[int]
        :rtype: List[List[int]]
        """
        indexs = list(range(0, len(groupSizes)))
        indexGroupSize = list(zip(groupSizes, indexs))
        indexGroupSize.sort()
        groups = []
        curGroup = []
        for demand in indexGroupSize:
            curGroup.append(demand[1])
            if len(curGroup) == demand[0]:
                groups.append(curGroup)
                curGroup = []

        return groups


if __name__ == '__main__':
    sol = Solution()
    print(sol.groupThePeople([3, 3, 3, 3, 3, 1, 3]))
