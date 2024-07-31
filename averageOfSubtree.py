# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def averageOfSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.nodes = 0

        self.dfs(root)
        return self.nodes

    def dfs(self, root):
        if not root:
            return 0, 0
        totalSum = root.val
        numNodes = 1
        leftSum, leftNodes = self.dfs(root.left)
        rightSum, rightNodes = self.dfs(root.right)
        totalSum += leftSum + rightSum
        numNodes += leftNodes + rightNodes
        if (totalSum // numNodes == root.val):
            self.nodes += 1
        return (totalSum, numNodes)


if __name__ == '__main__':
    root = TreeNode(4, TreeNode(8, TreeNode(0), TreeNode(1)), TreeNode(5, None, TreeNode(6)))
    sol = Solution()
    print(sol.averageOfSubtree(root))
