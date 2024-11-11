# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    pos = 0

    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        return self.traversal(root, k)

    def traversal(self, root, k):
        if not root:
            return -1
        num = self.traversal(root.left, k)
        if num != -1:
            return num
        self.pos += 1
        if k == self.pos:
            return root.val
        return self.traversal(root.right, k)


if __name__ == '__main__':
    tree = TreeNode(3, TreeNode(1, None, TreeNode(2)))
    sol = Solution()
    print(sol.kthSmallest(tree, 2))
