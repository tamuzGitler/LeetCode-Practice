class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        self.paths = []
        self.travel(graph, [0], 0)
        return self.paths

    def travel(self, graph, path, i):
        if i == len(graph) - 1:
            self.paths.append(path)
            return

        for node in graph[i]:
            self.travel(graph, path + [node], node)


if __name__ == '__main__':
    sol = Solution()
    graph = [[4, 3, 1], [3, 2, 4], [3], [4], []]
    print(sol.allPathsSourceTarget(graph))
