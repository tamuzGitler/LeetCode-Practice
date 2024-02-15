class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        i = 0
        stack = []

        while (i < len(num)):
            while k > 0 and stack and num[i] < stack[-1]:
                stack.pop()
                k -= 1
            if stack or num[i] != '0':
                stack.append(num[i])
            i += 1
        if k:
            stack = stack[:- k] # if monotonic, 12345... remove from the end


        return ''.join(stack) or '0'


if __name__ == '__main__':
    sol = Solution()
    num = "1432219"
    k = 3
    # print(sol.removeKdigits(num,k))

    num = "10200"
    k = 1
    print(sol.removeKdigits(num, k))

    num = "10"
    k = 2
    print(sol.removeKdigits(num, k))

    num = "112"
    k = 1
    print(sol.removeKdigits(num, k))
