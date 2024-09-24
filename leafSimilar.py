# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        order1, order2 = [], []
        self.dfs(root1, order1)
        self.dfs(root2, order2)
        if len(order1) != len(order2):
            return False
        for i in range(len(order1)):
            if order1[i] != order2[i]:
                return False
        return True

    def dfs(self, root, order):
        if not root:
            return
        if not root.left and not root.right:
            order.append(root.val)
        self.dfs(root.left, order)
        self.dfs(root.right, order)
