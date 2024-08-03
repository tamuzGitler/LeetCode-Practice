import sys


class Solution(object):
    def distributeCookies(self, cookies, k):
        """
        :type cookies: List[int]
        :type k: int
        :rtype: int
        """
        if len(cookies) == k:
            return max(cookies)
        chidsDistribution = [0] * k
        self.minUnfairness = sys.maxsize
        self.traverse(cookies, 0, chidsDistribution)
        return self.minUnfairness

    def traverse(self, cookies, j, chidsDistribution):
        if j > len(cookies) - 1:
            self.minUnfairness = min(max(chidsDistribution), self.minUnfairness)
            return

        for i in range(len(chidsDistribution)):
            chidsDistribution[i] += cookies[j]
            self.traverse(cookies, j + 1, chidsDistribution)
            chidsDistribution[i] -= cookies[j]


if __name__ == '__main__':
    cookies = [64, 32, 16, 8, 4, 2, 1, 1000]

    k = 8
    sol = Solution()
    print(sol.distributeCookies(cookies, k))
