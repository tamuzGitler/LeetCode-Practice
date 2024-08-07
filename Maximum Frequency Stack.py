import heapq
from collections import defaultdict


class FreqStack(object):

    def __init__(self):
        self.heap = []
        self.app = defaultdict(int)
        self.index = 0

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.app[val] += 1
        heapq.heappush(self.heap, (-self.app[val], -self.index, val))
        self.index += 1

    def pop(self):
        """
        :rtype: int
        """
        app, ind, val = heapq.heappop(self.heap)
        self.app[val] -= 1
        return val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()

if __name__ == '__main__':
    stack = FreqStack()
    stack.push(1)
    stack.push(2)
    stack.push(1)
    stack.push(3)
    stack.push(3)
    a = 5
    # stack.push(3)
    # stack.push(4)
    # stack.push(2)
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    # print(stack.pop())
    # print(stack.pop())
    # stack.push(1)
    # stack.push(1)
    # print(stack.pop())
