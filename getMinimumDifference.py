# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math


class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.minDiff = math.inf
        self.prev = None
        self.inorderTraversal(root)
        return self.minDiff

    def inorderTraversal(self, root):
        if not root:
            return

        self.inorderTraversal(root.left)
        if self.prev:
            self.minDiff = min(self.minDiff, abs(self.prev.val - root.val))
        self.prev = root
        self.inorderTraversal(root.right)
