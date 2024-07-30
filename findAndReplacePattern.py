class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        ans = []
        for word in words:
            d = dict()
            mapping_dict = dict()
            flag = True
            for key, val in zip(pattern, word):
                if key in mapping_dict:
                    if mapping_dict[key] != val:
                        flag = False
                        break
                else:
                    if val in mapping_dict.values():
                        flag = False
                        break
                    mapping_dict[key] = val
            if flag:
                ans.append(word)
        return ans

        #
        #     c = word[i]
        #     if c == pattern[i] and
        #     if c in d:
        #         if d[c] != pattern[i]:
        #             break
        #         else:


if __name__ == '__main__':
    words = ["abc", "deq", "mee", "aqq", "dkd", "ccc"]
    pattern = "abb"
    sol = Solution()
    print(sol.findAndReplacePattern(words, pattern))
