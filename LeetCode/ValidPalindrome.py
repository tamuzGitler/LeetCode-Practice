class Solution(object):
    # O(N) time , O(N) space, can be done in O(1) space!
    def isPalindromeClassic(self, s):
        """
        :type s: str
        :rtype: bool
        """
        pal = ""
        for letter in s:
            if not letter.isalpha() and not letter.isalnum():
                continue
            if letter.islower():
                pal += letter
            elif letter.isupper():
                pal += letter.lower()
            else:
                pal += letter
        for i in range(len(pal)// 2):
            if pal[i] != pal[len(pal)- i - 1]:
                return False
        return True
    # pointer solution
    def isPalindrome(self, s):
        left, right = 0, len(s) - 1
        while (left < right):
            while not self.isAlphaNumeric(s[left]) and left < right:
                left += 1
            while not self.isAlphaNumeric(s[right]) and left < right:
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True
    def isAlphaNumeric(self,c):
        return (ord('a') <= ord(c) <= ord('z') or
                ord('A') <= ord(c) <= ord('Z') or
                ord('0') <= ord(c) <= ord('9'))


if __name__ == '__main__':

    sol = Solution()
    s = "A man, a plan, a canal: Panama"
    s = "0P"
    s = ".,"
    print(sol.isPalindrome(s))