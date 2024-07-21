class StackImp:

    # empty
    # peek
    # pop
    # push
    # search
    def __init__(self):
        self._stack = []

    def isEmpty(self):
        return len(self._stack) == 0

    def peek(self):
        if not self.isEmpty():
            return self._stack[-1]
        else:
            return None  # or raise exception

    def pop(self):
        return self._stack.pop()

    def push(self, val):
        self._stack.append(val)
