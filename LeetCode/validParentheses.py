class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        openDic = {'(': ')', '{': '}', '[': ']'}
        for c in s:
            if c in openDic:
                stack.append(c)
            else:
                if not stack:
                    return False
                curOpener = stack.pop()
                if openDic[curOpener] != c:
                    return False

        return len(stack) == 0
