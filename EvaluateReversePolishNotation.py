import math


class Solution(object):
    def evalRPN2(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for token in tokens:
            if token == '+':
                topNum = stack.pop()
                stack[-1] += topNum
            elif token == '-':
                topNum = stack.pop()
                stack[-1] -= topNum
            elif token == '*':
                topNum = stack.pop()
                stack[-1] *= topNum
            elif token == '/':
                topNum = stack.pop()
                bottomNum = stack.pop()
                div = bottomNum / topNum
                if div < 0:
                    div = math.ceil(div)
                else:
                    div = bottomNum // topNum
                stack.append(div)
            else:  # token is number
                stack.append(int(token))
        return stack[0]
    # inplace
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        numPointer = 0
        tokens[0] = int(tokens[0])
        for i,token in enumerate(tokens[1:]):
            if token == '+':
                tokens[numPointer-1] = tokens[numPointer - 1] + tokens[numPointer]
                numPointer -= 1
            elif token == '-':
                tokens[numPointer-1] = tokens[numPointer - 1] - tokens[numPointer]
                numPointer -= 1
            elif token == '*':
                tokens[numPointer-1] = tokens[numPointer - 1] * tokens[numPointer]
                numPointer -= 1
            elif token == '/':
                tokens[numPointer - 1] = tokens[numPointer - 1] // tokens[numPointer] if (tokens[numPointer - 1] / tokens[numPointer]) >0 else math.ceil(tokens[numPointer - 1] / tokens[numPointer])
                numPointer -= 1
            else:  # token is number

                numPointer += 1
                tokens[numPointer] = int(token)
        return tokens[0]
if __name__ == '__main__':
    tokens = ["2", "1", "+", "3", "*"]
    tokens = ["4", "13", "5", "/", "+"]
    tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    sol = Solution()
    print(sol.evalRPN(tokens))
