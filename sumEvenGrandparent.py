# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def sumEvenGrandparent(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        grandparets = []
        self.evenGrandparent = 0
        self.dfs(root, None, None)
        return self.evenGrandparent

    def dfs(self, root, parent, grandpa):
        if not root:
            return
        if grandpa and grandpa % 2 == 0:
            self.evenGrandparent += root.val
        grandpa = parent
        parent = root.val

        self.dfs(root.left, parent, grandpa)
        self.dfs(root.right, parent, grandpa)


if __name__ == '__main__':
    # Create nodes based on the values in the image
    root = TreeNode(6)
    root.left = TreeNode(7)
    root.right = TreeNode(8)

    root.left.left = TreeNode(2)
    root.left.right = TreeNode(7)
    root.right.left = TreeNode(1)
    root.right.right = TreeNode(3)

    root.left.left.left = TreeNode(9)
    root.left.right.left = TreeNode(1)
    root.left.right.right = TreeNode(4)
    root.right.right.right = TreeNode(5)
    sol = Solution()
    print(sol.sumEvenGrandparent(root))
