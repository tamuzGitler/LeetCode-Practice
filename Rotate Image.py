class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        # transponse - (i,j) - (j,i)
        for i in range(len(matrix)):  # rows
            for j in range(i + 1):  # cols
                self.swap(matrix, (i, j), (j, i))

        # swap colums
        for i in range(len(matrix)):
            for j in range(len(matrix[0]) // 2):
                self.swap(matrix, (i, j), (i, len(matrix) - 1 - j))

    def swap(self, matrix, ind1, ind2):
        temp = matrix[ind1[0]][ind1[1]]
        matrix[ind1[0]][ind1[1]] = matrix[ind2[0]][ind2[1]]
        matrix[ind2[0]][ind2[1]] = temp
        a = 5


if __name__ == '__main__':
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    sol = Solution()
    sol.rotate(matrix)
