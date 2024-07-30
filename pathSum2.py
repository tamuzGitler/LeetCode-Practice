# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):

    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: List[List[int]]
        """
        if not root:
            return []
        l = []
        ans = []
        self.dfs(root, targetSum, l, ans)
        return ans

    def dfs(self, root, targetSum, l, ans):
        if not root:
            return
        l.append(root.val)
        targetSum -= root.val

        if (not root.left and not root.right):

            if targetSum == 0:
                ans.append(l[:])
        self.dfs(root.left, targetSum, l, ans)
        self.dfs(root.right, targetSum, l, ans)

        l.pop()


if __name__ == '__main__':
    sol = Solution()
    root = TreeNode(5, TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))),
                    TreeNode(8, TreeNode(13), TreeNode(4, TreeNode(5), TreeNode(1))))
    print(sol.pathSum(root, 22))
