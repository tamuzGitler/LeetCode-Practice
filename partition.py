class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        ans = [list(s)]
        

if __name__ == '__main__':
    s = 'aab'
    sol = Solution()
    print(sol.partition(s))
