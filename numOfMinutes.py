import collections
from collections import deque


class Solution(object):
    def numOfMinutes(self, n, headID, manager, informTime):
        """
        :type n: int
        :type headID: int
        :type manager: List[int]
        :type informTime: List[int]
        :rtype: int
        """
        adj = collections.defaultdict(list)  # manager -> his employes
        for curManager in range(n):
            adj[manager[curManager]].append(curManager)
        q = deque([(headID, 0)])
        res = 0
        while q:
            curManager, time = q.popleft()
            res = max(res, time)
            for emp in adj[curManager]:
                q.append((emp, time + informTime[curManager]))

        return res


if __name__ == '__main__':
    n = 11

    headID = 4
    manager = [5, 9, 6, 10, -1, 8, 9, 1, 9, 3, 4]

    informTime = [0, 213, 0, 253, 686, 170, 975, 0, 261, 309, 337]

    sol = Solution()
    print(sol.numOfMinutes(n, headID, manager, informTime))
