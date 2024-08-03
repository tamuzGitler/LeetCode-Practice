# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):

    def distributeCoins(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.moves = 0
        self.dfs(root)
        return self.moves

    def dfs(self, node):
        if not node:
            return 0
        leftCoins = self.dfs(node.left)
        rightCoins = self.dfs(node.right)

        self.moves += abs(leftCoins) + abs(rightCoins)
        return (node.val - 1) + leftCoins + rightCoins


if __name__ == '__main__':
    root = TreeNode(0, TreeNode(0), TreeNode(3))
    sol = Solution()
    print(sol.distributeCoins(root))
