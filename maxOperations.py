from collections import Counter


class Solution(object):

    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        s, e = 0, len(nums) - 1
        maxOps = 0
        while s < e:
            pairSum = nums[s] + nums[e]
            if pairSum == k:
                maxOps += 1
                s += 1
                e -= 1
            elif pairSum > k:
                e -= 1
            else:
                s += 1
        return maxOps

    # def maxOperations(self, nums, k):
    #     """
    #     :type nums: List[int]
    #     :type k: int
    #     :rtype: int
    #     """
    #     maxOps = 0
    #     d = Counter(nums)
    #     removedFlag = True
    #     while d and removedFlag:
    #         removedFlag = False
    #         for key in list(d.keys()):
    #             pair = (k - int(key))
    #             while (pair != key and pair in d.keys() and key in d.keys()) or (pair == key and d[key] >= 2):
    #
    #                 d[pair] -= 1
    #                 d[key] -= 1
    #                 if d[pair] == 0:
    #                     del d[pair]
    #                 if d[key] == 0:
    #                     del d[key]
    #                 maxOps += 1
    #                 removedFlag = True
    #     return maxOps


if __name__ == '__main__':
    nums = [3, 1, 3, 4, 3]
    k = 6
    sol = Solution()
    print(sol.maxOperations(nums, k))
