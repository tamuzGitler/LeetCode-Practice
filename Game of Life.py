import copy


class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """

        boardCopy = copy.deepcopy(board)
        for row in range(len(board)):
            for col in range(len(board[0])):
                livesCells = self.getLiveNeighbors(boardCopy, row, col)
                if boardCopy[row][col] == 1:
                    if livesCells < 2 or livesCells > 3:
                        board[row][col] = 0
                elif livesCells == 3:
                    board[row][col] = 1

    def getLiveNeighbors(self, boardCopy, row, col):
        livesCells = 0
        if row == 0:
            if col == 0:
                livesCells += boardCopy[row][col + 1] + boardCopy[row + 1][col] + boardCopy[row + 1][col + 1]
            elif col == len(boardCopy[0]) - 1:
                livesCells += boardCopy[row][col - 1] + boardCopy[row + 1][col - 1] + boardCopy[row + 1][col]
            else:
                livesCells += boardCopy[row][col - 1] + boardCopy[row][col + 1] + boardCopy[row + 1][col - 1] + \
                              boardCopy[row + 1][col] + boardCopy[row + 1][col + 1]
        elif row == len(boardCopy) - 1:
            if col == 0:
                livesCells += boardCopy[row - 1][col] + boardCopy[row - 1][col + 1] + boardCopy[row][col + 1]
            elif col == len(boardCopy[0]) - 1:
                livesCells += boardCopy[row - 1][col - 1] + boardCopy[row - 1][col] + boardCopy[row][col - 1]
            else:
                livesCells += boardCopy[row][col - 1] + boardCopy[row][col + 1] + boardCopy[row - 1][col - 1] + \
                              boardCopy[row - 1][col] + boardCopy[row - 1][col + 1]
        else:
            if col > 0 and col < len(boardCopy[0]) - 1:
                livesCells += boardCopy[row][col - 1] + boardCopy[row][col + 1] + boardCopy[row + 1][col - 1] + \
                              boardCopy[row + 1][col] + boardCopy[row + 1][col + 1] + boardCopy[row - 1][col - 1] + \
                              boardCopy[row - 1][col] + boardCopy[row - 1][col + 1]
            elif col == 0:
                livesCells += + boardCopy[row][col + 1] + \
                              boardCopy[row + 1][col] + boardCopy[row + 1][col + 1] + \
                              boardCopy[row - 1][col] + boardCopy[row - 1][col + 1]
            elif col == len(boardCopy[0]) - 1:
                livesCells += boardCopy[row][col - 1] + boardCopy[row + 1][col - 1] + \
                              boardCopy[row + 1][col] + boardCopy[row - 1][col - 1] + \
                              boardCopy[row - 1][col]
        return livesCells


if __name__ == '__main__':
    board = [[0, 0]]
    sol = Solution()
    sol.gameOfLife(board)
    print(board)
