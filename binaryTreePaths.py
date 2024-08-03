# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        self.ans = []
        self.dfs(root, "")
        return self.ans

    def dfs(self, root, s):
        if not root:
            return
        if not root.left and not root.right:
            self.ans.append(s + str(root.val))

        self.dfs(root.left, s + str(root.val) + "->")
        self.dfs(root.right, s + str(root.val) + "->")


if __name__ == '__main__':
    sol = Solution()
    root = TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3))
    print(sol.binaryTreePaths(root))
