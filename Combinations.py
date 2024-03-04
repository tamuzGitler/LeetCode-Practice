class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        sub = []
        i = 1
        self.helper(n,i,k,res,sub)
        return res

    def helper(self,n,i,k,res,sub):
        if i > n and len(sub) != k :
            return

        if len(sub) == k :
            res.append(sub.copy())
        else:
            sub.append(i)
            # if len(arr) != 1:
            self.helper(n,i+1,k,res,sub)
            sub.pop()
            self.helper(n,i+1, k, res, sub)

if __name__ == '__main__':
    n = 4
    k = 2
    sol = Solution()
    print(sol.combine(n,k))



