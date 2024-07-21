import math


class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        low = 1
        high = max(piles)
        while (low <= high):
            k = low + (high - low) // 2
            if self.finishEatingBeforeTime(piles,h,k):
                high = k - 1
            else:
                low = k +  1
        return low

    def finishEatingBeforeTime(self, piles, h, k):
        hours = 0
        for pile in piles:
            hours += math.ceil(pile / k)
        return hours <= h


if __name__ == '__main__':
    piles = [30, 11, 23, 4, 20]
    h = 6
    sol = Solution()
    print(sol.minEatingSpeed(piles, h))
