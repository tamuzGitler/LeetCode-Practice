class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        ans = ''
        i = 0
        while (i < len(s)):
            endInd = i
            while s[endInd].isdigit():
                endInd += 1
            if i != endInd:
                stack.append(s[i:endInd])
            c = s[i]
            i = endInd

            if c == ']':
                curStr = ''
                addCurStr = True
                while stack:
                    val = stack.pop()
                    if val.isdigit():
                        curStr = int(val) * curStr
                        if stack:
                            stack.append(curStr)
                            addCurStr = False
                            break
                    else:
                        curStr = val + curStr
                if addCurStr:
                    ans = ans + curStr
            elif c.isalpha():
                stack.append(c)
            i += 1
        postFix = ''
        while stack:
            postFix = stack.pop() + postFix
        ans += postFix
        return ans


if __name__ == '__main__':
    s = "3[a]2[bc]"
    s = "3[a2[c]]"
    # s = "2[abc]3[cd]ef"
    # s = "100[leetcode]"
    # s = "3[z]2[2[y]pq4[2[jk]e1[f]]]ef"

    sol = Solution()
    print(sol.decodeString(s))
