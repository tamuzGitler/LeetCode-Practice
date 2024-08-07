from collections import defaultdict


class Solution(object):
    def maximumImportance(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        apperances = defaultdict(int)
        for c1, c2 in roads:
            apperances[c1] += 1
            apperances[c2] += 1
        apperances = sorted(apperances.items(), key=lambda item: item[1], reverse=True)
        cityDict = dict()
        sum = 0
        for city, apperance in apperances:
            cityDict[city] = n
            sum += n * apperance
            n -= 1

        return sum


if __name__ == '__main__':
    n = 5
    roads = [[0, 3], [2, 4], [1, 3]]
    sol = Solution()
    print(sol.maximumImportance(n, roads))
