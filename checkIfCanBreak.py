class Solution(object):
    def checkIfCanBreak(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """

        arr1 = [0] * 26
        arr2 = [0] * 26

        flag1 = True
        flag2 = True
        for c in s1:
            arr1[ord(c) - 97] += 1
        for c in s2:
            arr2[ord(c) - 97] += 1

        j = 0
        k = 0
        for i in range(len(s1)):
            while arr1[j] == 0:
                j += 1

            while arr2[k] == 0:
                k += 1

            if j < k:
                flag1 = False
            if j > k:
                flag2 = False
            arr1[j] -= 1
            arr2[k] -= 1
        return flag1 or flag2


if __name__ == '__main__':
    s1 = "abe"

    s2 = "acd"

    sol = Solution()
    print(sol.checkIfCanBreak(s1, s2))
