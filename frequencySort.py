class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        my_dict = dict()
        for c in s:
            my_dict[c] = my_dict.get(c, 0) + 1
        sorted_items = sorted(my_dict.items(), key=lambda item: item[1], reverse=True)  # Reverse sorting
        ans = ''
        for key, val in sorted_items:
            ans += key * val
        return ans


if __name__ == '__main__':
    s = "tree"
    sol = Solution()
    print(sol.frequencySort(s))
