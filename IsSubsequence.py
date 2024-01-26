class Solution(object):
    def isSubsequence(self, s, t):
        """
        return true if s is a subsequence of t, or false otherwise.
        :type s: str
        :type t: str
        :rtype: bool
        """
        sInd,tInd = 0,0
        while(sInd < len(s) and tInd < len(t)):
            if t[tInd] == s[sInd]:
                sInd += 1
            tInd +=1
        return sInd == len(s)
if __name__ == '__main__':
    sol = Solution()
    s = "abc"
    t = "ahbgdc"
    print(sol.isSubsequence(s,t))