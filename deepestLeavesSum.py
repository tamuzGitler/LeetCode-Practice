# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def deepestLeavesSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        stack = [[root]]
        while stack:
            nodes = stack.pop()
            nextLvl = []
            lvlSum = 0
            for node in nodes:
                lvlSum += node.val
                if node.left:
                    nextLvl.append(node.left)
                if node.right:
                    nextLvl.append(node.right)
            if not nextLvl:
                return lvlSum
            else:
                stack.append(nextLvl)
