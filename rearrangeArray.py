class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        pos = []
        neg = []
        for num in nums:
            if num > 0:
                pos.append(num)
            else:
                neg.append(num)
        return self.merge(pos,neg)

    def merge(self, pos, neg):
        j,k =0,0
        ans = []
        for i in range(len(pos) + len(neg)):
            if i % 2 == 0:
                ans.append(pos[j])
                j += 1
            else:
                ans.append(neg[k])
                k += 1
        return ans

