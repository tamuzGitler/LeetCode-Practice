class Solution(object):
    def findArray(self, pref):
        """
        :type pref: List[int]
        :rtype: List[int]
        """
        arr = [pref[0]]
        for i in range(len(pref) - 1):
            arr.append(pref[i] ^ pref[i + 1])

        return arr


if __name__ == '__main__':
    sol = Solution()
    # pref = [413935, 351122]
    # arr = [5,7,2,3,2]
    print(sol.findArray(pref))
