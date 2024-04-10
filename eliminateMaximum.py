import math


class Solution(object):
    def eliminateMaximum(self, dist, speed):
        """
        :type dist: List[int]
        :type speed: List[int]
        :rtype: int
        """
        for i,d in enumerate(dist):
            dist[i] = math.ceil(d / speed[i])
        dist.sort()
        for i in range(len(dist)):
            if dist[i] <= i:
                return i

        return len(dist)


if __name__ == '__main__':
    dist = [1, 3, 4]
    speed = [1, 1, 1]
    sol = Solution()
    print(sol.eliminateMaximum(dist,speed))