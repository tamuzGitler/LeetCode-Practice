class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        self.order = []
        # if len(matrix) == 1:
        #     for col in range(len(matrix[0])):
        #         self.order.append(matrix[0][col])
        #     return self.order
        # elif len(matrix[0]) == 1:
        #     for row in range(len(matrix)):
        #         self.order.append(matrix[row][0])
        #     return self.order
        self.traverse(matrix)
        return self.order

    def traverse(self, matrix):
        bottom = len(matrix) - 1
        right = len(matrix[0]) - 1
        top = 0
        left = 0

        while (left <= right and top <= bottom):
            # 1 - iterate over cols (right)
            for col in range(left, right + 1):
                self.order.append(matrix[top][col])
            top += 1
            # 2 - iterate over rows | (down)
            for row in range(top, bottom + 1):
                self.order.append(matrix[row][right])
            right -= 1

            # 3 - iterate over rows | (left)
            if top <= bottom:
                for col in range(right, left - 1, -1):
                    self.order.append(matrix[bottom][col])
                bottom -= 1

            # 4 - iterate over rows | (up)
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    self.order.append(matrix[row][left])
                left += 1


if __name__ == '__main__':
    # matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    # matrix = [[3], [2]]
    # matrix = [[2, 5, 8], [4, 0, -1]]

    sol = Solution()
    print(sol.spiralOrder(matrix))
