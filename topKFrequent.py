import heapq


class Solution(object):
    # def topKFrequent2(self, nums, k):
    #     """
    #     :type nums: List[int]
    #     :type k: int
    #     :rtype: List[int]
    #     """
    #     heap = []
    #     d = dict()
    #     for num in nums:
    #         d[num] = d[num] + 1 if num in d else 1
    #     for num, freq in d.items():
    #         heapq.heappush(heap, (freq, num))
    #         if len(heap) > k:
    #             heapq.heappop(heap)
    #     return [num for freq, num in heap]
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        counter = [None] * (len(nums) + 1)
        d = dict()
        ans = []
        for num in nums:
            d[num] = d[num] + 1 if num in d else 1
        for num, freq in d.items():
            if not counter[freq]:
                counter[freq] = [num]
            else:
                counter[freq].append(num)
        for i in range(len(counter) - 1, 0, -1):
            if counter[i]:
                for num in counter[i]:
                    ans.append(num)
                    if len(ans) == k:
                        return ans
        return ans


if __name__ == '__main__':
    sol = Solution()
    nums = [1]
    k = 1
    print(sol.topKFrequent(nums, k))
