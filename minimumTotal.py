class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        ans = [[0]]
        for i in range(len(triangle)):
            curLevel = []
            for j, pathCost in enumerate(triangle[i]):
                min(ans[-1])
