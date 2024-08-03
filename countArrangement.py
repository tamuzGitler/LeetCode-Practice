class Solution(object):
    def countArrangement(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.beautifulArrangements = 0
        perm = list(range(1, n + 1))
        self.traverse(1, perm, n)
        return self.beautifulArrangements

    def traverse(self, i, perm, n):
        if i > n:
            self.beautifulArrangements += 1

            return

        for permI in perm.copy():
            if permI % i == 0 or i % permI == 0:
                perm.remove(permI)
                self.traverse(i + 1, perm.copy(), n)
                perm.append(permI)


if __name__ == '__main__':
    n = 5
    sol = Solution()
    print(sol.countArrangement(n))
