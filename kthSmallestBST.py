# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    val = None

    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.k = k
        self.traversal(root)
        return self.val

    def traversal(self, root):
        if (not root):
            return -1
        self.traversal(root.left)
        self.k -= 1
        if self.k == 0:
            self.val = root.val
        self.k += 1
        self.traversal(root.right)
