class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        subset = []
        self.dfs( candidates, res, subset, target)
        return res
    def dfs(self, candidates, res, subset, target):
        # if not candidates or sum(subset) > target:
        #     return
        if not candidates or sum(subset) > target:
            return
        if sum(subset) == target:
            # if subset not in res:
            res.append(subset.copy())
            return
        else:
            subset.append(candidates[0])
            self.dfs(candidates, res, subset, target) # maybe add candidates[0] again

            subset.pop()
            self.dfs(candidates[1:], res, subset, target) # add but continue to next candidate



if __name__ == '__main__':
    sol = Solution()
    candidates = [2, 3, 6, 7]
    target = 7
    print(sol.combinationSum(candidates,target))
