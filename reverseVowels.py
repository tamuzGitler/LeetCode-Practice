class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        i, j = 0, len(s) - 1
        vowels = {'a', 'e', 'i', 'o', 'u'}
        while i < j:
            while s[i].lower() not in vowels and i < j:
                i += 1
            while s[j].lower() not in vowels and i < j:
                j -= 1
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        return "".join(s)


if __name__ == '__main__':
    s = "IceCreAm"
    sol = Solution()
    print(sol.reverseVowels(s))
