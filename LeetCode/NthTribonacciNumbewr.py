class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        T = [0,1,1]
        for i in range(3,n+1):
            T.append(sum(T[i-3:i]))
        return T[n]
if __name__ == '__main__':
    sol = Solution()
    print(sol.tribonacci(3))
    print(sol.tribonacci(4))
    print(sol.tribonacci(5))
    print(sol.tribonacci(6))
    print(sol.tribonacci(7))
    print(sol.tribonacci(25))
