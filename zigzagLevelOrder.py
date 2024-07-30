# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        leftFlag = False
        stack = [[root]]
        ans = [[root.val]]
        while (stack):
            nodes = stack.pop()
            childs = []
            childsVals = []
            for node in nodes:

                if node.left:
                    childs.append(node.left)
                    childsVals.append(node.left.val)
                if node.right:
                    childs.append(node.right)
                    childsVals.append(node.right.val)

            if len(childs) != 0:
                stack.append(childs)
                if leftFlag:
                    ans.append(childsVals)
                else:
                    ans.append(childsVals[::-1])
                leftFlag = not leftFlag
        return ans


if __name__ == '__main__':
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    sol = Solution()
    ans = sol.zigzagLevelOrder(root)
