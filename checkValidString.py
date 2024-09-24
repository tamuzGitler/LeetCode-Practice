class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        openP = 0
        i = 0
        return self.backTrack(s, openP, i)

    def backTrack(self, s, openP, i):

        if i >= len(s):
            return True if openP == 0 else False
        if s[i] == ')':
            if openP <= 0:
                return False
            openP -= 1
            return self.backTrack(s, openP, i + 1)
        elif s[i] == '(':
            openP += 1
            return self.backTrack(s, openP, i + 1)
        else:  # *
            # * = ') case

            return self.backTrack(s, openP + 1, i + 1) or self.backTrack(s, openP - 1, i + 1) or self.backTrack(s,
                                                                                                                openP,
                                                                                                                i + 1)


if __name__ == '__main__':
    s = "((((()(()()()*()(((((*)()*(**(())))))(())()())(((())())())))))))(((((())*)))()))(()((*()*(*)))(*)()"
    sol = Solution()
    print(sol.checkValidString(s))
