class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if len(citations) == 1:
            return 1 if citations[0] > 0 else 0
        citations.sort()
        h = 0
        for i in range(len(citations)):
            if citations[i] >= len(citations) - i:
                h = max(len(citations) - i, h)
        return h


if __name__ == '__main__':
    citations = [3, 0, 6, 1, 5]
    citations = [1, 3, 1]
    citations = [11, 15]
    sol = Solution()
    print(sol.hIndex(citations))
