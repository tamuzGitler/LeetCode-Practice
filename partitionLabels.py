class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        charsRange = dict()
        for i, curChar in enumerate(s):
            if curChar in charsRange:
                charsRange[curChar][1] = i
            else:
                charsRange[curChar] = [i, i]
        ans = []

        while (charsRange):
            removeChars = set()
            start, end = -1, -1
            for curChar in charsRange:
                if start == -1 and end == -1:
                    start, end = charsRange[curChar]
                    removeChars.add(curChar)

                elif charsRange[curChar][0] >= start and charsRange[curChar][0] <= end:
                    end = max(charsRange[curChar][1], end)
                    removeChars.add(curChar)
            ans.append(end - start + 1)
            for c in removeChars:
                del charsRange[c]
        return ans


if __name__ == '__main__':
    sol = Solution()
    s = "ababcbacadefegdehijhklij"
    print(sol.partitionLabels(s))
