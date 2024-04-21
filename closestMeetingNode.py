import math


class Solution(object):
    def closestMeetingNode(self, edges, node1, node2):
        """
        :type edges: List[int]
        :type node1: int
        :type node2: int
        :rtype: int
        """
        node1Map = {node1: 0}
        node2Map = {node2: 0}
        dist1 = 1
        dist2 = 1
        temp1 = node1
        while (edges[node1] != -1):
            if edges[node1] not in node1Map:
                node1Map[edges[node1]] = dist1
                node1 = edges[node1]
                dist1 += 1
            else:
                break
        node1 = temp1
        while (edges[node2] != -1):
            if edges[node2] not in node2Map:
                node2Map[edges[node2]] = dist2
                node2 = edges[node2]
                dist2 += 1
            else:
                break
        maxDis = math.inf
        retNode = -1
        for key in node1Map.keys():
            if key in node2Map.keys():
                curDist = max(node1Map[key], node2Map[key])
                if curDist < maxDis:
                    maxDis = curDist
                    retNode = key
                elif curDist == maxDis:  # return node with smallest index!
                    retNode = min(key, retNode)

        return retNode


if __name__ == '__main__':
    edges = [2, 2, 3, -1]
    node1 = 0
    node2 = 1
    edges = [1, 2, -1]
    node1 = 2
    node2 = 0
    edges = [2, 0, 0]

    # edges = [5, 3, 1, 0, 2, 4, 5]
    #
    # node1, node2 = 3, 2
    # edges = [9, 8, 7, 0, 5, 6, 1, 3, 2, 2]
    # node1, node2 = 1, 6
    sol = Solution()
    print(sol.closestMeetingNode(edges, node1, node2))
