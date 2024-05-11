# Definition for a Node.
from collections import deque


class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return root
        stack = deque()
        parents = deque()
        parents.append(root)
        stack.append(parents)
        while stack:
            childs = deque()
            parents = stack.pop()
            prev = None
            while parents:
                parent = parents.popleft()
                parent.next = prev
                prev = parent
                if parent.left and parent.right:
                    childs.append(parent.right)
                    childs.append(parent.left)
            if childs:
                stack.append(childs)
        return root


if __name__ == '__main__':
    root = Node(1, Node(2), Node(3))
    sol = Solution()
    sol.connect(root)
    a = 5
