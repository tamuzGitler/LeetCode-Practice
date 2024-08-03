import heapq


class SmallestInfiniteSet(object):

    def __init__(self):
        self.heap = list(range(1, 1001))
        heapq.heapify(self.heap)
        self.removed = set(self.heap)

    def popSmallest(self):
        """
        :rtype: int
        """
        retVal = heapq.heappop(self.heap)
        self.removed.remove(retVal)
        return retVal

    def addBack(self, num):
        """
        :type num: int
        :rtype: None
        """
        if num not in self.removed:
            heapq.heappush(self.heap, num)
            self.removed.add(num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)

if __name__ == '__main__':
    obj = SmallestInfiniteSet()
    print(obj.popSmallest())
    print(obj.popSmallest())
    print(obj.popSmallest())
    print(obj.popSmallest())
    obj.addBack(1)
    print(obj.popSmallest())
    print(obj.popSmallest())
    print(obj.popSmallest())
    print(obj.popSmallest())
    print(obj.popSmallest())
    print(obj.popSmallest())
    print(obj.popSmallest())
    print(obj.popSmallest())
    print(obj.popSmallest())
    obj.addBack(100)
    print(obj.popSmallest())
