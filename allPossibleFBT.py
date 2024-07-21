# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def allPossibleFBT(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        #  2^h - 1
        treeInHeight = [[None],[TreeNode(0)], [TreeNode(0,TreeNode(0),TreeNode(0))]]
        for i in range(2,n):
            for j in range(len(TreeNode)):

