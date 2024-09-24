class Solution(object):
    def chalkReplacer(self, chalk, k):
        """
        :type chalk: List[int]
        :type k: int
        :rtype: int
        """
        i = 0
        k = k % sum(chalk)
        while chalk[i % len(chalk)] <= k:
            k -= chalk[i % len(chalk)]
            i += 1
        return i


if __name__ == '__main__':
    chalk = [3, 4, 1, 2]
    k = 25

    sol = Solution()
    print(sol.chalkReplacer(chalk, k))
