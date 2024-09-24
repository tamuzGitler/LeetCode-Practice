class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        maxCandies = max(candies)
        ans = []
        for candy in candies:
            ans.append(candy + extraCandies >= maxCandies)
        return ans
