import random


class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.shuffledNums = nums[:]

    def reset(self):
        """
        :rtype: List[int]
        """

        return self.nums

    def shuffle(self):
        """
        :rtype: List[int]
        """
        self.shuffledNums = self.nums[:]
        random.shuffle(self.shuffledNums)
        return self.shuffledNums


if __name__ == '__main__':
    nums = [1, 2, 3]
    sol = Solution(nums)
    print(sol.shuffle())
    print(sol.reset())
    print(sol.shuffle())
    print(sol.shuffle())
    print(sol.shuffle())
    print(sol.shuffle())
