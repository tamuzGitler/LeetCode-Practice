# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.dfs(root)[0]
    def dfs(self,root):
        if not root:
            return [True,0]
        left,right = self.dfs(root.left), self.dfs(root.right)
        balanced = left[0] and right[0] and abs(left[1] - right[1]) <=1
        return [balanced, 1 + max(left[1], right[1])]

if __name__ == '__main__':
    root = TreeNode(1, left=TreeNode(2,left=TreeNode(3,left=TreeNode(4),right=TreeNode(4)),right=TreeNode(3)),right=TreeNode(2))
    root2= TreeNode(1,TreeNode(2))
    sol = Solution()
    print(sol.isBalanced(root))
    print(sol.isBalanced(root2))
