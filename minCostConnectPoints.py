class Solution(object):
    class Edge:
        def __init__(self, v1, v2, cost):
            self.v1 = v1
            self.v2 = v2
            self.cost = cost

        # def __eq__(self, other):
        #     return self.cost <= other.cost
        #
        # def __hash__(self):
        #     return hash(self.cost)

    class unionFind:
        def __init__(self):
            self.sets = set()

        def find(self, vertex):
            for set in self.sets:
                if vertex in set:
                    return set
            return None

        def union(self, set1):
            self.sets.union(set1)

    class Graph:
        def __init__(self):
            self.vertexs = set()
            self.edges = list()

        def addEdge(self, v1, v2, manhatanCost):
            self.edges.append(Solution.Edge(v1, v2, manhatanCost))
            self.vertexs.add(v1)
            self.vertexs.add(v2)

        def find(self, v1):
            for set in self.edges:
                for edge in set:
                    if v1 == edge.v1 or v1 == edge.v2:
                        return set
            return None

        def union(self, set1):
            self.sets.union(set1)

    def minCostConnectPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        graph = self.Graph()
        for v1 in range(len(points)):
            for v2 in range(v1 + 1, len(points)):
                manhatanCost = abs(points[v1][0] - points[v2][0]) + abs(points[v1][1] - points[v2][1])
                graph.addEdge(v1, v2, manhatanCost)
        graph.edges = (sorted(graph.edges, key=lambda edge: edge.cost))

        print(graph.find(v1))
        for edge in graph.edges:
            pass
        return 0


if __name__ == '__main__':
    points = [[2, -3], [-17, -8], [13, 8], [-17, -15]]

    sol = Solution()
    print(sol.minCostConnectPoints(points))
