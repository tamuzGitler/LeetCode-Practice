# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """

        if not root or not subRoot:
            return False
        if root.val == subRoot.val:
            if self.checkSub(root.left, subRoot.left) and self.checkSub(root.right, subRoot.right):
                return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    def checkSub(self,root,subRoot):
        if not root and not subRoot:
            return True
        if (not root and subRoot) or (root and not subRoot) or (root.val != subRoot.val):
            return False
        return self.checkSub(root.left,subRoot.left) and self.checkSub(root.right, subRoot.right)