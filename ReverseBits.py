class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        s = str(bin(n))[2:]
        s = "0b" + s[::-1]
        return s

if __name__ == '__main__':
    # sol = Solution()
    # print(sol.reverseBits(n=43261596))
    k = int(6)
    t = k & ~(1 << 2)
    print(t)