class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        mergedString = ""
        i, j = 0, 0
        flag = True
        for i in range(min(len(word1), len(word2))):
            mergedString += word1[i] + word2[i]
        if len(word1) < len(word2):
            mergedString += word2[len(word1):]
        else:
            mergedString += word1[len(word2):]

        return mergedString
