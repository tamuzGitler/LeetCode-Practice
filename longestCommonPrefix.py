class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        if len(strs) == 1:
            return strs[0]
        prefix = ''
        # get shortest prefix
        for word in strs:
            if len(word) > len(prefix):
                prefix = word
        while (prefix):
            longestPrefixFlag = True
            for word in strs:
                if prefix != word[0:len(prefix)]:
                    longestPrefixFlag = False
                    prefix = prefix[0:len(prefix) - 1]
                    break
            if longestPrefixFlag:
                return prefix
        return prefix
