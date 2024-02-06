class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        warmerTemperature = [0] * len(temperatures)
        stack = []
        for index,temperature in enumerate(temperatures):
            while stack and stack[-1][0] < temperature:
                topTemerature, topIndex = stack[-1]
                if topTemerature < temperature:
                    warmerTemperature[topIndex] = (index - topIndex)
                    stack.pop()

            stack.append((temperature,index))
        return warmerTemperature

if __name__ == '__main__':
    temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    sol = Solution()
    print(sol.dailyTemperatures(temperatures))
