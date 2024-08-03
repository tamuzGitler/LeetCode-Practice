class Solution(object):
    def getMaximumGold(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        maxGold = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                maxGold = max(self.backTrack(grid, i, j, 0), maxGold)
        return maxGold

    def outOfBound(self, grid, i, j):
        return (i < 0 or i > len(grid) - 1 or j < 0 or j > len(grid[0]) - 1)

    def backTrack(self, grid, i, j, goldCollected):
        if self.outOfBound(grid, i, j) or grid[i][j] == 0:
            return goldCollected
        goldCollected += grid[i][j]
        originalGoldValue = grid[i][j]
        grid[i][j] = 0  # mark as visited
        goldCollected = max(self.backTrack(grid, i - 1, j, goldCollected),
                            self.backTrack(grid, i + 1, j, goldCollected),
                            self.backTrack(grid, i, j - 1, goldCollected),
                            self.backTrack(grid, i, j + 1, goldCollected))
        grid[i][j] = originalGoldValue  # restore cell to its original value

        return goldCollected


if __name__ == '__main__':
    grid = [[1, 0, 7, 0, 0, 0], [2, 0, 6, 0, 1, 0], [3, 5, 6, 7, 4, 2], [4, 3, 1, 0, 2, 0], [3, 0, 5, 0, 20, 0]]
    sol = Solution()
    print(sol.getMaximumGold(grid))
