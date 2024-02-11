import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = list(nums[0:k])
        heapq.heapify(minHeap)

        for num in (nums[k:]):
            heapq.heappushpop(minHeap,num)
        return heapq.heappop(minHeap)