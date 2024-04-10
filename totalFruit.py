class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        lastSeen = fruits[0]
        lastSeenStarting = 0
        startInd = 0
        maxInterval = 0
        secondNum = None
        for i in range(1, len(fruits)):
            num = fruits[i]
            if secondNum != None and (num != lastSeen and num != secondNum):
                maxInterval = max(maxInterval, i - startInd)
                secondNum = lastSeen  # fruits[i-1]
                lastSeen = num
                startInd = lastSeenStarting
                lastSeenStarting = i

            elif num == secondNum:
                secondNum = lastSeen
                lastSeen = num
                lastSeenStarting = i
            elif secondNum == None and num != lastSeen:

                secondNum = lastSeen
                lastSeenStarting = i
                lastSeen = num
        maxInterval = max(maxInterval, len(fruits) - startInd)
        return maxInterval


if __name__ == '__main__':
    # fruits = [1, 2, 1]
    # fruits = [0, 1, 0, 2]
    fruits = [0, 1, 2, 2]
    fruits = [1, 2, 3, 2, 2]
    fruits = [3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]
    fruits = [0, 0, 1, 1]

    sol = Solution()
    print(sol.totalFruit(fruits))
