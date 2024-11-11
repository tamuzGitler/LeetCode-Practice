# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math


class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        return self.traverse(root.left, -math.inf, root.val) and self.traverse(root.right, root.val, math.inf)

    def traverse(self, root, minVal, maxVal):
        if not root:
            return True
        if root.val <= minVal or root.val >= maxVal:
            return False
        return self.traverse(root.left, minVal, root.val) and self.traverse(root.right, root.val, maxVal)
