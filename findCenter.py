class Solution(object):
    def findCenter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        seenVertex = set()
        for Vi, Ui in edges:
            if Vi in seenVertex:
                return Vi
            if Ui in seenVertex:
                return Ui
            seenVertex = seenVertex.union({Vi, Ui})


if __name__ == '__main__':
    edges = [[1, 2], [2, 3], [4, 2]]
    sol = Solution()
    print(sol.findCenter(edges))
