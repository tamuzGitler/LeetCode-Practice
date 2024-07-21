class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        d = dict()
        dups = []
        for i in range(len(s) - 9):
            print(i)
            sub = s[i:i + 10]
            if sub in d:
                if d[sub] == 1:
                    dups.append(sub)
                d[sub] += 1


            else:
                d[sub] = 1
        return dups


if __name__ == '__main__':
    s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
    s = "AAAAAAAAAAA"
    print(len(s))
    sol = Solution()
    print(sol.findRepeatedDnaSequences(s))
