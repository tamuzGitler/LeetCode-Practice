class Solution(object):
    def numOfPairs(self, nums, target):
        """
        :type nums: List[str]
        :type target: str
        :rtype: int
        """
        d = dict()
        for num in nums:
            d[num] = d.get(num, 0) + 1

        # 123:2
        # 4:1
        pairs = 0
        for num in nums:

            prefix = target[:len(num)].replace(num, "") + target[len(num):]
            if prefix in d:
                if prefix == num:
                    pairs -= 1
                pairs += d[prefix]
        return pairs


if __name__ == '__main__':
    nums = ["123", "4", "123"]

    target = ("1234"
              "")

    sol = Solution()
    print(sol.numOfPairs(nums, target))
