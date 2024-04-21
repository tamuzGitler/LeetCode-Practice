class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        self.ans = set()
        if len(s) <= 12:
            self.helper(s, '', 0)
        return self.ans

    def addIp(self, s, ip):
        if ip[-1] != '.' and not s:
            self.ans.add(ip)

    def helper(self, s, ip, dots):
        if not s:
            return
        for i in range(1, 4):
            if 0 <= int(s[:i]) <= 255:
                newIp = ip + s[:i]
                if dots < 3:
                    self.helper(s[i:], newIp + '.', dots + 1)
                else:
                    self.addIp(s[i:], newIp)
            if s[0] == '0':
                if i == 1:
                    return


if __name__ == '__main__':
    s = "25525511135"
    # s = "0000"
    # s = "101023"
    sol = Solution()
    print(sol.restoreIpAddresses(s))
