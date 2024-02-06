class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        stack = []
        for operation in operations:
            if operation == "+":
                top = stack.pop()
                bottom = stack.pop()
                newScore = top + bottom
                stack.append(bottom)
                stack.append(top)
                stack.append(newScore)

            elif operation == "D":
                top = stack.pop()
                doubleScore = top * 2
                stack.append(top)
                stack.append(doubleScore)
            elif operation == "C":
                stack.pop()
            else:  # number
                stack.append(int(operation))

        return sum(stack)

if __name__ == '__main__':
    operations = ["5","2","C","D","+"]
    sol = Solution()
    print(sol.calPoints(operations))