class Solution(object):

    def kthSmallestPrimeFraction(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: List[int]
        """
        fractions = []
        hashMap = dict()
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                hashMap[arr[i] / arr[j]] = [arr[i], arr[j]]
        sortedMap = sorted(hashMap.items())
        return sortedMap[k - 1][1]


if __name__ == '__main__':
    arr = [1, 2, 3, 5]
    k = 3
    sol = Solution()
    print(sol.kthSmallestPrimeFraction(arr, k))
