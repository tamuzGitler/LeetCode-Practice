class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        binaryRep = str(bin(n)[2:])
        return binaryRep.count(1)


if __name__ == '__main__':
    sol = Solution()
    print(sol.hammingWeight(2))
