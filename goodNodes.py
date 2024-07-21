# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


import math


class Solution(object):
    counter = 0

    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.inorderTraversal(root, math.inf)
        return self.counter

    def inorderTraversal(self, root, prevMaxNode):
        if not root:
            return
        if root.val >= prevMaxNode:
            self.counter += 1
        prevMaxNode = max(prevMaxNode, root.val)
        self.inorderTraversal(root.left, prevMaxNode)
        self.inorderTraversal(root.right, prevMaxNode)


if __name__ == '__main__':
    root = TreeNode(3, TreeNode(1, TreeNode(3)), TreeNode(4, TreeNode(1), TreeNode(5)))
    sol = Solution()
    print(sol.goodNodes(root))
