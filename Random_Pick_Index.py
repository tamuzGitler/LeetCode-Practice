from collections import defaultdict
import random


class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.numIndexs = defaultdict(list)
        for i, num in enumerate(nums):
            self.numIndexs[num].append(i)
        a = 5

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        possibleIndexs = self.numIndexs[target]
        return random.choice(possibleIndexs)


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
if __name__ == '__main__':
    nums = [1, 2, 3, 3, 3]
    sol = Solution(nums)
    print(sol.pick(3))
    print(sol.pick(3))
    print(sol.pick(3))
    print(sol.pick(3))
