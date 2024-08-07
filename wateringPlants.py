class Solution(object):
    def wateringPlants(self, plants, capacity):
        """
        :type plants: List[int]
        :type capacity: int
        :rtype: int
        """
        steps = 0
        curCapacity = capacity
        for i in range(len(plants)):
            if curCapacity - plants[i] >= 0:
                steps += 1
            else:
                curCapacity = capacity
                steps += 2 * i + 1
            curCapacity -= plants[i]
        return steps


if __name__ == '__main__':
    plants = [2, 2, 3, 3]
    capacity = 5
    sol = Solution()
    print(sol.wateringPlants(plants, capacity))
