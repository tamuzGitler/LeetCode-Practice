class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        self.nums = list(nums)
        self.nums.sort()

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        start, end = 0, len(self.nums) - 1
        mid = 0
        while (start < end):
            mid = (end - start // 2) + start
            if val > self.nums[mid] and val < self.nums[mid + 1]:
                break
            elif val < self.nums[mid]:
                end = mid -1
            else:
                start = mid + 1
        self.nums.insert(mid, val)
        return self.nums[-3]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
if __name__ == '__main__':
    kthLargest = KthLargest(3, [4, 5, 8, 2])
    print(kthLargest.add(3))
    print(kthLargest.add(5))
    print(kthLargest.add(10))
    print(kthLargest.add(9))
    print(kthLargest.add(4))
