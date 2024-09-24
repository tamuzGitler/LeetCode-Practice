class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        increase = 0
        maxRows = [max(row) for row in grid]
        maxCol = []
        for col in range(len(grid[0])):  # Iterate over each column
            column_values = [row[col] for row in grid]  # Extract values from the column
            maxCol.append(max(column_values))
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                increase += min((maxRows[row]), (maxCol[col])) - grid[row][col]

        return increase


if __name__ == '__main__':
    grid = [[3, 0, 8, 4], [2, 4, 5, 7], [9, 2, 6, 3], [0, 3, 1, 0]]
    sol = Solution()
    print(sol.maxIncreaseKeepingSkyline(grid))
