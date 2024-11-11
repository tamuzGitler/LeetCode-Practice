class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        posCombinations = list()
        ans = list()
        candidates.sort()
        self.backTrack(candidates, target, posCombinations, 0, ans)

        return ans

    def backTrack(self, canidates, target, posCombinations, index, ans):
        if target == 0:
            ans.append(posCombinations[:])
            return

        for i in range(index, len(canidates)):
            if i > index and canidates[i] == canidates[i - 1]:
                continue
            if canidates[i] > target:
                break

            posCombinations.append(canidates[i])
            self.backTrack(canidates, target - canidates[i], posCombinations, i + 1, ans)
            posCombinations.pop()


if __name__ == '__main__':
    candidates = [10, 1, 2, 1, 7, 6, 1, 5]

    target = 8
    sol = Solution()
    print(sol.combinationSum2(candidates, target))

    1, 1, 1, 1, 2, 3
    1, 2, 1, 1, 3, 1, 1
