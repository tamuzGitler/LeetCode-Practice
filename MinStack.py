class MinStack(object):

    def __init__(self):
        self.stack = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        if not self.stack:
            self.stack.append(Node(val, val))
        else:
            curMin = min(val, self.stack[-1].min)
            self.stack.append(Node(val, curMin))

    def pop(self):
        """
        :rtype: None
        """
        if self.stack:
            self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1].val

    def getMin(self):
        """
        :rtype: int
        """
        return self.stack[-1].min


class Node:
    def __init__(self, val, min):
        self.val = val
        self.min = min


if __name__ == '__main__':
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    print(minStack.getMin())  # return -3
    minStack.pop()
    print(minStack.top())  # return 0
    print(minStack.getMin())  # return -2
