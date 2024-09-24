class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxWater = 0
        s, e = 0, len(height) - 1
        while s < e:
            maxWater = max(maxWater, (e - s) * min(height[s], height[e]))
            if height[s] < height[e]:
                s += 1
            else:
                e -= 1
        return maxWater


if __name__ == '__main__':
    sol = Solution()
    height = [1, 8, 6, 100, 100, 4, 8, 3, 7]
    print(sol.maxArea(height))
