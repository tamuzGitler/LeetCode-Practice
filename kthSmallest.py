import heapq


class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        heap = []
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if len(heap) == k:
                    if heap[-1] <= -matrix[i][j]:
                        heapq.heappop(heap)
                        heapq.heappush(heap, -matrix[i][j])
                else:
                    heapq.heappush(heap, -matrix[i][j])
        return -heapq.heappop(heap)


if __name__ == '__main__':
    matrix = [[1, 4], [2, 5]]
    sol = Solution()
    print(sol.kthSmallest(matrix, 2))
