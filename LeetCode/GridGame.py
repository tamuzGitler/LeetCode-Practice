class Solution(object):
    def gridGame(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        self.minimize_score(grid)
        secondPlayerPoints = self.maximize_score(grid)
        return secondPlayerPoints

    def minimize_score(self, grid):
        row, col = 1, len(grid[0]) - 1
        points = grid[row][col]
        grid[row][col] = 0
        while (row != 0 or col != 0):
            if col == 0:
                row -= 1

            elif row == 0 or grid[row][col - 1] >= grid[row - 1][col]:
                col -= 1
            else:
                row -= 1
            points += grid[row][col]
            grid[row][col] = 0

    def maximize_score(self, grid):
        row, col = 0, 0
        points = grid[row][col]

        while (row < 2 and col < len(grid[0])-1):
            if row == 0 and col < len(grid[0])-2:
                if  grid[row+1][col] > grid[row][col+1]:
                    row += 1
                else:
                    col += 1
            elif row == 1:
                col+=1

            else:
                row += 1
            points += grid[row][col]
        return points




if __name__ == '__main__':
    grid1 = [[2,5,4],[1,5,1]]
    grid2 = [[3,3,1],[8,5,2]]
    grid3 = [[1,3,1,15],[1,3,3,1]]
    grid4 = [[20,3,20,17,2,12,15,17,4,15],
             [20,10,13,14,15,5,2,3,14,3]]
    sol = Solution()
    secondPlayerPoints = sol.gridGame(grid4)
    print(secondPlayerPoints)