class Solution(object):


    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = 0

        for i in range(len(s)-1,-1,-1):

            if s[i] == " ":
                if length != 0:
                    return length
            else:
                length += 1
        return length

    # def lengthOfLastWord(self, s):
    #     """
    #     :type s: str
    #     :rtype: int
    #     """
    #     st = s.split(' ')
    #     while "" in st and st[-1] == "":
    #
    #         st.remove("")
    #     return len(st[-1])

if __name__ == '__main__':
    s = "hello world"
    s = "a"
    # s ="   fly me   to   the moon  "
    sol = Solution()
    print(sol.lengthOfLastWord(s))
    a = ""
    b=5