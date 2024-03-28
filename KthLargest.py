import heapq


class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        self.nums = nums
        heapq.heapify(self.nums)
        while (len(self.nums) > k):  # after this the min value in heap is k largest elem
            heapq.heappop(self.nums)

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        heapq.heappush(self.nums, val)
        if len(self.nums) > self.k:
            heapq.heappop(self.nums)
        return self.nums[0]
        # k_elem = heapq.heappop( self.nums)
        # if k_elem > val:
        #     heapq.heappush( self.nums,val)
        #     return k_elem
        # else:
        #     heapq.heappush(self.nums,k_elem)
        #     return heapq.heappop(self.nums)


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
if __name__ == '__main__':
    k = 3
    nums = [4, 5, 8, 2]
    obj = KthLargest(k, nums)
    print(obj.add(3))
    print(obj.add(5))
    print(obj.add(10))
    print(obj.add(9))
    print(obj.add(4))
