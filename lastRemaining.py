import math


class Solution(object):
    # def helper(self,arr, isLeft):
    #     n = len(arr)
    #     if (len(arr) == 1):
    #         return arr[0]
    #     ans = []
    #     if isLeft:
    #         for i in range(1, n, 2):
    #             ans.append(arr[i])
    #     else:
    #         for i in range(n - 2, -1, -2):
    #             ans.insert(0,arr[i])
    #     return self.helper(ans, not isLeft)
    #
    # def lastRemaining2(self, n):
    #     """
    #     :type n: int
    #     :rtype: int
    #     """
    #     if n == 1:
    #         return 1
    #     return self.helper(list(range(1, n+1)), True)

    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """

        s,e = 1,n
        jump = 1
        isLeft = True
        while ( s != e):
            diff = math.ceil(e / jump)
            if isLeft:
                s += jump
                if diff % 2 != 0:
                    e -= jump
            else:
                e -= jump
                if diff % 2 != 0:
                    s += jump
            jump *= 2
            isLeft = not isLeft
        return s


if __name__ == '__main__':
    sol = Solution()
    # print(sol.lastRemaining(1))
    # print(sol.lastRemaining(2))
    # print(sol.lastRemaining(3))
    # print(sol.lastRemaining(4))
    # print(sol.lastRemaining(5))
    # print(sol.lastRemaining(6))
    # print(sol.lastRemaining(7))
    # print(sol.lastRemaining(8))
    print(sol.lastRemaining(9))
    # print(sol.lastRemaining(10))
    # print(sol.lastRemaining(11))
    # print(sol.lastRemaining(12))
    # print(sol.lastRemaining(13))
    # print(sol.lastRemaining(14))
    # print(sol.lastRemaining(15))
    # print(sol.lastRemaining(16))
    # print(sol.lastRemaining(17))
    # # 1,2,3,4,5,6,7,8
    # 2,4,6,8
    # 2,6
    # 6