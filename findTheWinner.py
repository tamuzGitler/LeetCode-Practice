class Solution(object):
    def findTheWinner(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        players = list(range(1, n + 1))
        start = 0
        while (len(players) > 1):
            index = (k - 1 + start) % len(players)
            start = index
            players.pop(index)
        return players[0]


if __name__ == '__main__':
    sol = Solution()
    print(sol.findTheWinner(5, 2))
