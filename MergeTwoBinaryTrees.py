# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    #O(N) + O(M) - N,M size of root1 and root2 trees
    def mergeTrees(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: TreeNode
        """
        if not root1 and not root2:
            return None
        root = TreeNode(self.nodesSum(root1,root2))
        root.left = self.mergeTrees(root1.left if root1 else None, root2.left if root2 else None)
        root.right = self.mergeTrees(root1.right if root1 else None, root2.right if root2 else None)
        return root

    def nodesSum(self,root1,root2):
        if root1 and root2:
            return root1.val + root2.val
        elif not root1:
            return root2.val
        return root1.val

if __name__ == '__main__':
    root1 = TreeNode(1)
    root2 = TreeNode(1,TreeNode(4))
    sol = Solution()
    root = sol.mergeTrees(root1,root2)
    ans = 0