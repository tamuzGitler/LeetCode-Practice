class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        self.cols = len(word1) + 1
        self.rows = len(word2) + 1
        self.dp = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        self.initDpTable()

        self.fillTable(word1, word2)

        return self.dp[-1][-1]

    def fillTable(self, word1, word2):
        for row in range(1, self.rows):
            for col in range(1, self.cols):

                # do nothing
                if word1[col - 1] == word2[row - 1]:
                    self.dp[row][col] = self.dp[row - 1][col - 1]
                    continue
                # Insert
                insertOps = self.dp[row - 1][col]

                # Delete
                delete = self.dp[row][col - 1]

                # Replace
                replace = self.dp[row - 1][col - 1]

                self.dp[row][col] = min(insertOps, delete, replace) + 1

    def initDpTable(self):
        # fill first row - with delition operation - converting word1[0:i] into ""
        for col in range(1, self.cols):
            self.dp[0][col] = col

        # fill first col - with insertion operation - converting "" into word2[0,j]
        for row in range(1, self.rows):
            self.dp[row][0] = row


if __name__ == '__main__':
    sol = Solution()
    print(sol.minDistance(word1="horse", word2="ros"))
