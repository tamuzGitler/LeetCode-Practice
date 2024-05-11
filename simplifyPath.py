class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []
        i = 0
        p = path.split('/')
        for s in p:
            if not s:
                continue
            elif s == '.':
                continue
            elif s == '..':  # remove prev dict if it exists
                if stack:
                    stack.pop()
            else:
                stack.append(s)
        return '/' + '/'.join(stack)


if __name__ == '__main__':
    sol = Solution()
    path = "/home/"
    path = "/home//foo/"
    path = "/home/user/Documents/../Pictures"
    path = "/../"
    # path = "/.../a/../b/c/../d/./"
    # path = "/a/./b/../../c/"
    # path = '/.'

    print(sol.simplifyPath(path))
