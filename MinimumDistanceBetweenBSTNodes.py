# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
import math


class Solution(object):
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return
        left = abs(root.val - root.left) if root.left else 2147483647
        right = abs(root.val - root.right) if root.right else 2147483647
        return min(left,right,self.minDiffInBST(root.left), self.minDiffInBST(root.right))
        # self.curr_smallest, self.prev = 2147483647, None # max int
        #
        # def inorder(node):
        #
        #     if node is None:
        #         return
        #
        #     inorder(node.left)
        #     if self.prev is not None:
        #         self.curr_smallest = min(self.curr_smallest, abs(node.val - self.prev.val))
        #     self.prev = node
        #     inorder(node.right)
        #
        # inorder(root)
        # return int(self.curr_smallest)
def print_tree(node):
    if node:
        print(node.val)
        print_tree(node.left)
        print_tree(node.right)

if __name__ == '__main__':
    sol = Solution()
    # root = TreeNode(4,TreeNode(2,TreeNode(0),TreeNode(3)),TreeNode(6))
    # Create the tree
    root = TreeNode(90)
    root.left = TreeNode(69)
    root.left.left = TreeNode(49)
    root.right = TreeNode(89)
    root.right.right = TreeNode(52)
    print(sol.minDiffInBST(root))
    # print_tree(root)

