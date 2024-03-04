class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        return self.helper(board, word, 0, 0, 0, used=set())

    def helper(self, board, word, i, row, col, used):
        if i >= len(word):
            return True
        elif (row, col) in used:
            return False
        used.add((row, col))

        if (row < 0 or col < 0 or row >= len(board) or col >= len(board[0])):
            return False
        if board[row][col] == word[0]:
            i += 1

        return (self.helper(board, word, i, row - 1, col, used) or self.helper(board, word, i, row + 1, col,
                                                                               used) or
                self.helper(board, word, i, row, col - 1, used) or self.helper(board, word, i, row, col + 1,
                                                                               used))

if __name__ == '__main__':
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "ABCCED"
    sol = Solution()
    print(sol.exist(board,word))