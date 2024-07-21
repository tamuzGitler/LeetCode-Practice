class Solution:
    def searchMatrix(self, matrix, target) :
        if target > matrix[-1][-1] or target < matrix[0][0]:
            return False
        row = self.binaryRowSearch(matrix,target,0, len(matrix)-1)
        matrixRow = matrix[row]
        return self.binarySearch(matrixRow, target, 0, len(matrixRow)-1)
    def binarySearch(self, row, target, start, end):
        while(start <= end):
            mid = start + (end - start) // 2
            if row[mid] == target:
                return True
            elif target < row[mid]:
                end = mid - 1
            else:
                start = mid + 1
        return False


    def binaryRowSearch(self, matrix, target, start, end):
        while(start <= end):
            mid = start + (end - start) // 2
            if (target >= matrix[mid][0] and target <= matrix[mid][-1]):
                return mid
            if (target < matrix[mid][0]):
                end = mid - 1
            else:
                start = mid + 1
        return start

if __name__ == '__main__':
    matrix = [[1], [3]]
    target = 2
    sol = Solution()
    # print(sol.binaryRowSearch(matrix,target,0,len(matrix)))
    print(sol.searchMatrix(matrix,target))