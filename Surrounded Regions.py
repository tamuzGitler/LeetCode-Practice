class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        for row in range(1, len(board) - 1):
            for col in range(1, len(board[0]) - 1):
                if board[row][col] == 'O':
                    if self.shouldNotFlip(board, row, col):
                        continue
                    else:
                        board[row][col] = 'X'

    def shouldNotFlip(self, board, row, col):
        if ((row - 1 == 0 and board[row - 1][col] == 'O') or (
                row + 1 == len(board) - 1 and board[row + 1][col] == 'O') or
                (col - 1 == 0 and board[row][col - 1] == 'O') or (col + 1 == len(board[0]) - 1) and board[row][
                    col + 1] == 'O'):
            return True

        return board[row - 1][col] == 'O' and board[row + 1][col] == 'O' and board[row][col - 1] == 'O' and board[row][
            col + 1] == 'O'


if __name__ == '__main__':
    board = [["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]]
    # board = [["X", "O", "X"], ["X", "O", "X"], ["X", "O", "X"]]
    sol = Solution()
    sol.solve(board)
    print(board)
