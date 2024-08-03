class Solution(object):
    def letterCasePermutation(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        self.ans = [
        ]
        self.traverse(s, 0, '')
        return self.ans

    def traverse(self, s, i, curS):
        if i == len(s) - 1:
            if s[i].isalpha():
                if s[i].isupper():
                    self.ans.append(curS + s[i].lower())
                else:
                    self.ans.append(curS + s[i].upper())
            self.ans.append(curS + s[i])
            return

        if s[i].isalpha():
            if s[i].isupper():
                self.traverse(s, i + 1, curS + s[i].lower())
            else:
                self.traverse(s, i + 1, curS + s[i].upper())
        self.traverse(s, i + 1, curS + s[i])


if __name__ == '__main__':
    s = "C"
    print(Solution().letterCasePermutation(s))
