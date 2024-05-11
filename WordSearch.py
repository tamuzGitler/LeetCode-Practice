class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        visited = set()
        for i in range(len(board)):
            for j in range(len(board[0])):

                if self.helper(board, word, i, j, visited):  # every starting pos
                    return True
        return False

    def helper(self, board, word, i, j, visited):
        if len(word) == 0:
            return True
        if not self.legalIndex(board, i, j) or word[0] != board[i][j] or (i, j) in visited:
            return False
        visited.add((i, j))
        if len(word) == 1:
            return True
        word = word[1:]
        res = self.helper(board, word, i - 1, j, visited) or self.helper(board, word, i + 1, j,
                                                                         visited) or self.helper(board, word, i, j - 1,
                                                                                                 visited) or self.helper(
            board, word, i, j + 1, visited)
        visited.remove((i, j))
        return res

    def legalIndex(self, board, i, j):
        return ((i >= 0) and i < len(board)) and (j >= 0 and j < len(board[0]))


if __name__ == '__main__':
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "ABCCED"
    sol = Solution()
    print(sol.exist(board, word))
