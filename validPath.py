from collections import defaultdict


class Solution(object):
    def validPath(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """
        if n == 1:
            return True
        d = defaultdict(list)
        for u, v in edges:
            d[u].append(v)
            d[v].append(u)
        visited = set()

        def dfs(node):
            neighbours = d[node]

            for neighbour in neighbours:
                if neighbour == destination:
                    visited.add(neighbour)
                    break
                if neighbour not in visited:
                    visited.add(neighbour)
                    dfs(neighbour)

        dfs(source)
        return destination in visited


if __name__ == '__main__':
    edges = [[0, 7], [0, 8], [6, 1], [2, 0], [0, 4], [5, 8], [4, 7], [1, 3], [3, 5], [6, 5]]
    source = 7
    n = 10
    destination = 5
    sol = Solution()
    print(sol.validPath(n, edges, source, destination))
