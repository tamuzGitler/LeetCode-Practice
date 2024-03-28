class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """

        if n == 0 or (len(flowerbed) == 1 and flowerbed[0] == 0 and n == 1):
            return True
        flowerbed = [0] + flowerbed + [0]
        for i in range(1, len(flowerbed) - 1):
            if n == 0:
                return True
            if sum(flowerbed[i - 1:i + 2]) == 0:
                flowerbed[i] = 1
                n -= 1

        return n == 0


if __name__ == '__main__':
    sol = Solution()
    # flowerbed = [1, 0, 0, 0, 1]
    # n = 1
    flowerbed = [1, 0, 0, 0, 1]
    # n = 2
    flowerbed = [0, 0, 0, 0, 1]
    flowerbed = [1, 0, 0, 0, 1, 0, 0]

    # flowerbed = [1,0]
    # flowerbed = [0,0,0]
    # flowerbed = [0]

    n = 2

    print(sol.canPlaceFlowers(flowerbed, n))
