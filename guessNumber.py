# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):


class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        start, end = 1, n
        ans = -1
        while (ans != 0):
            myGuess = start + (end - start) // 2
            ans = guess(myGuess)
            if ans == -1:
                start = myGuess + 1
            elif ans == 1:
                end = myGuess - 1
        return myGuess
