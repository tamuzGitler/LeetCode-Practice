class Solution(object):
    def partitionString(self, s):
        """
        :type s: str
        :rtype: int
        """
        curSet = set()
        partitions = 1
        for c in s:
            if c in curSet:
                partitions += 1
                curSet.clear()
            curSet.add(c)
        return partitions


if __name__ == '__main__':
    s = "abacaba"
    sol = Solution()
    print(sol.partitionString(s))
