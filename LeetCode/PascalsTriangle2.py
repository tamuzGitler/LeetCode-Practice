class Solution(object):
    # uses O(rowIndex) space, not saving the hall triangle, just the previous row
    def getRow(self, rowIndex):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        pascalTriangle = [1]
        for i in range(rowIndex ):
            prevRow = [0] + pascalTriangle + [0]
            prev = 0
            row = []
            for j in range(len(prevRow)-1):
                cur = prevRow[j+1]
                row.append(prev + cur)
                prev = cur
            pascalTriangle = row
        return pascalTriangle


if __name__ == '__main__':
    sol = Solution()
    print(sol.getRow(rowIndex=0))
    print(sol.getRow(rowIndex=1))
    print(sol.getRow(rowIndex=2))
    print(sol.getRow(rowIndex=3))
    print(sol.getRow(rowIndex=4))
    print(sol.getRow(rowIndex=5))