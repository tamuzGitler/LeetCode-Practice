class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        if len(chars) == 1:
            return 1
        s, e = 0, 0
        while e < len(chars):
            count = 1
            while e < len(chars) - 1 and chars[e] == chars[e + 1]:
                count += 1
                e += 1
            chars[s] = chars[e]
            s += 1
            if count > 1:
                for val in str(count):
                    chars[s] = val
                    s += 1
            e += 1

        del chars[s:]
        return len(chars)


if __name__ == '__main__':
    chars = ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]

    sol = Solution()
    print(sol.compress(chars))
