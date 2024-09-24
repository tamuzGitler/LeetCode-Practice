class Solution(object):
    def findThePrefixCommonArray(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        commonPrefix = [0] * len(A)
        s1 = set()
        s2 = set()
        prev = 0
        for i in range(len(A)):

            if A[i] == B[i]:
                commonPrefix[i] = 1 + (commonPrefix[i - 1] if i > 0 else 0)

            s1.add(A[i])
            s2.add(B[i])

            if A[i] != B[i]:
                if A[i] in s2:
                    commonPrefix[i] += 1
                if B[i] in s1:
                    commonPrefix[i] += 1
                commonPrefix[i] += (commonPrefix[i - 1] if i > 0 else 0)
        return commonPrefix


if __name__ == '__main__':
    A = [2, 3, 1]

    B = [3, 1, 2]

    sol = Solution()
    print(sol.findThePrefixCommonArray(A, B))
