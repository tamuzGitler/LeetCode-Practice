from math import comb


class Solution(object):
    def threeSumMulti(self, arr, target):
        """
        :type arr: List[int]
        :type target: int
        :rtype: int
        """
        arr.sort()
        mults = 0
        for s in range(len(arr) - 2):
            m = s + 1
            e = len(arr) - 1
            while (m < e):
                sum = arr[s] + arr[m] + arr[e]
                if sum == target:
                    if arr[m] == arr[e]:
                        mults += comb(e - m + 1, 2)
                        break
                    else:
                        tempM = m + 1
                        while (arr[tempM] == arr[m]):
                            tempM += 1
                        tempE = e - 1
                        while (arr[tempE] == arr[e]):
                            tempE -= 1
                        mults += comb((e - tempE) + (tempM - m) + 2, 2)
                        m = tempM
                        e = tempE

                elif sum > target:
                    e -= 1
                elif sum < target:
                    m += 1
        return mults


if __name__ == '__main__':
    arr = [1, 1, 2, 2, 2, 2]
    target = 5
    sol = Solution()
    print(sol.threeSumMulti(arr, target))
