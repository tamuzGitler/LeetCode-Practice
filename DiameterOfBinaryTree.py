# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    maxDiameter = 0

    def diameterOfBinaryTree(self, root):
        """
        the diameter of root can be calculated:
        1. from combination of the (leftHeight + rightHeight + 2) - 2 to go to each side of tree
        2. from only one side of tree
        :type root: TreeNode
        :rtype: int
        """
        self.dfs(root)
        return self.maxDiameter

    def dfs(self, root):
        if not root:
            return -1  # null node has height of -1 and not 0!
        leftHeight = self.dfs(root.left)
        rightHeight = self.dfs(root.right)
        # 2 + leftHeight + rightHeight -> is the diameter between left and right sub tree of root
        self.maxDiameter = max(self.maxDiameter, 2 + leftHeight + rightHeight)
        return 1 + max(leftHeight, rightHeight)  # Height of root


if __name__ == '__main__':
    root = TreeNode(1, TreeNode(2))
    sol = Solution()
    print(sol.diameterOfBinaryTree(root))
