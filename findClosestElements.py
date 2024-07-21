class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """

        i = 0
        while i < len(arr) and arr[i] < x:
            i += 1

        if i < k:
            start, end = 0, k
        else:
            start, end = i - k, i
        while end < len(arr):
            a, b = arr[start], arr[end]

            if (abs(a - x) < abs(b - x)) or (abs(a - x) == abs(b - x) and a < b):
                break
            else:
                start += 1
                end += 1
        return arr[start:end]


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5]
    arr = [1, 2, 5, 5, 6, 6, 7, 7, 8, 9]

    k = 7
    x = 7
    sol = Solution()
    print(sol.findClosestElements(arr, k, x))
