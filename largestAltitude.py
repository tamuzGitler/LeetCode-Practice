class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        highestAltitude = 0
        curAlt = 0
        for g in gain:
            curAlt += g
            highestAltitude = max(highestAltitude, curAlt)
        return highestAltitude
