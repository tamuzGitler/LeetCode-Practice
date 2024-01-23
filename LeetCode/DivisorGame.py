class Solution(object):
    def divisorGame(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # alice_turn = True
        # while ( n != 1):
        #     n = (n - 1)
        #     if alice_turn:
        #         alice_turn = False
        #     else:
        #         alice_turn = True
        # return not alice_turn
        return not (n % 2 == 0)
if __name__ == '__main__':
    sol = Solution()
    print(sol.divisorGame(1))
    print(sol.divisorGame(2))
    print(sol.divisorGame(3))
    print(sol.divisorGame(4))
    print(sol.divisorGame(5))