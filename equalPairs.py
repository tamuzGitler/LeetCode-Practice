import hashlib


class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        pairs = 0
        d = dict()
        for row in grid:
            hashVal = (hashlib.sha256(bytes(str(row), 'utf-8')).hexdigest())
            d[hashVal] = d.get(hashVal, 0) + 1
        for col in zip(*grid):
            hashVal = hashlib.sha256(bytes(str(list(col)), 'utf-8')).hexdigest()
            if hashVal in d:
                pairs += d.get(hashVal)
        return pairs


if __name__ == '__main__':
    grid = [[3, 1, 2, 2], [1, 4, 4, 5], [2, 4, 2, 2], [2, 4, 2, 2]]

    sol = Solution()
    print(sol.equalPairs(grid))
