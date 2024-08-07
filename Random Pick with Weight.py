import random


class Solution(object):

    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.w = w
        sumW = sum(w)
        self.ranges = []
        lowerEdge = 0
        for i in range(len(w)):
            curProb = w[i] / sumW
            self.ranges.append([lowerEdge, curProb + lowerEdge])
            lowerEdge += curProb
        a = 5

    def pickIndex(self):
        """
        :rtype: int
        """
        prob = random.random()
        return self.binarySearch(prob, 0, len(self.ranges) - 1)

    def binarySearch(self, prob, start, end):
        mid = start + (end - start) // 2
        lowerBound, upperBound = self.ranges[mid]
        if prob >= lowerBound and prob <= upperBound:
            return mid
        elif prob < lowerBound:
            return self.binarySearch(prob, start, mid - 1)
        return self.binarySearch(prob, mid + 1, end)


if __name__ == '__main__':
    w = [1, 2, 3]
    sol = Solution(w)
    print(sol.pickIndex())
    print(sol.pickIndex())
    print(sol.pickIndex())
    print(sol.pickIndex())
    print(sol.pickIndex())

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
