class Solution(object):
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        dp = {}  # max score alice can get, dp[0, len(piles) - 1] max score she can get in the entire game

        def pickStone(start, end):
            if start > end:
                return 0
            if (start, end) in dp:
                return dp[(start, end)]
            even = True if (end - start) % 2 else False
            left = piles[start] if even else 0
            right = piles[end] if even else 0
            dp[(start, end)] = max(pickStone(start + 1, end) + left, pickStone(start, end - 1) + right)
            return dp[(start, end)]

        pickStone(0, len(piles) - 1)
        return dp[0, len(piles) - 1] > sum(piles) / 2


if __name__ == '__main__':
    piles = [3, 7, 2, 3]
    sol = Solution()
    print(sol.stoneGame(piles))
