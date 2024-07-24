class Solution(object):
    strings = []

    def validStrings(self, n):
        strings = []

        def helper(s):
            if len(s) == n:
                strings.append(s)
            elif len(s) == 0:
                helper('0')
                helper('1')
            else:
                if s[-1] != '0':
                    helper(s + '0')
                helper(s + '1')

        helper("")
        return strings
   

if __name__ == '__main__':
    sol = Solution()
    # print(sol.validStrings(0))
    # print(sol.validStrings(1))
    # print(sol.validStrings(2))
    print(sol.validStrings(3))
