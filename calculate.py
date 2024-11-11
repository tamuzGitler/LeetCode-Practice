class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []

        for i in range(len(s)):
            if s[i] == "+":
                self.calculate(s[i + 1:])
                stack.append(stack.pop() + stack.pop())
            elif s[i] == '-':
                self.calculate(s[i + 1:])
                stack.append(stack.pop() + stack.pop())
            elif s[i] == '(':
                self.calculate(s[i + 1:])
            elif s[i] == ')':
                pass
            else:
                stack.append(s[i])
