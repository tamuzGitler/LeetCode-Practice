class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        visited = {0}

        def dfs(key):
            roomKeys = rooms[key]
            for room in roomKeys:
                if len(visited) == len(rooms):
                    break
                if room not in visited:
                    visited.add(room)
                    dfs(room)

        dfs(0)
        return len(visited) == len(rooms)


if __name__ == '__main__':
    rooms = [[1], [2], [3], []]
    sol = Solution()
    print(sol.canVisitAllRooms(rooms))
