class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        operands = set()
        operands.add("+")
        operands.add("-")
        operands.add("*")
        operands.add("/")
        for token in tokens:
            if token not in operands:
                stack.append(int(token))
            elif token == "+":
                second = stack.pop()
                first = stack.pop()
                stack.append(first + second)
            elif token == "-":
                second = stack.pop()
                first = stack.pop()
                stack.append(first - second)
            elif token == "*":
                second = stack.pop()
                first = stack.pop()
                stack.append(first * second)
            elif token == "/":
                second = stack.pop()
                first = stack.pop()
                stack.append(int(first / second))
        return stack[-1]
