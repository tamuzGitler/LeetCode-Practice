class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        ans = []

        for i, interval in enumerate(intervals):
            curStart, curEnd = interval
            if newInterval[1] < curStart:
                ans.append(newInterval)
                return ans + intervals[i:]
            elif newInterval[0] > curEnd:
                ans.append(interval)
            else:  # over lap
                newInterval = [min(newInterval[0], curStart), max(newInterval[1], curEnd)]
        ans.append(newInterval)  # never added newInterval because it start after the end of last interval
        return ans


if __name__ == '__main__':
    intervals = [[1, 3], [6, 9]]
    newInterval = [2, 5]
    # intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
    # newInterval = [4, 8]
    # intervals = [[1, 5]]
    # newInterval = [0, 0]
    # intervals = [[3, 5], [12, 15]]
    # newInterval = [6, 6]
    # intervals = [[1, 2], [3, 4], [5, 6]]
    # newInterval = [2.5, 2.8]
    sol = Solution()
    print(sol.insert(intervals, newInterval))
