class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        pascalTriangle = [[1]]
        for i in range(numRows - 1):
            prevRow = [0] + pascalTriangle[i] + [0]
            prev = 0
            row = []
            for j in range(len(prevRow)-1):
                cur = prevRow[j+1]
                row.append(prev + cur)
                prev = cur
            pascalTriangle.append(row)
        return pascalTriangle


if __name__ == '__main__':
    sol = Solution()
    print(sol.generate(numRows=1))
    print(sol.generate(numRows=2))
    print(sol.generate(numRows=3))
    print(sol.generate(numRows=4))
    print(sol.generate(numRows=5))