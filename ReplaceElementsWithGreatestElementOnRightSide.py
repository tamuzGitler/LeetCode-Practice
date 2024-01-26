class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        ans = [-1]
        for val in arr[::-1][:len(arr)-1]:
            if val > ans[0]:
                ans.insert(0,val)
            else:
                ans.insert(0,ans[0])
        return ans
    def replaceElements2(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        arr.append(-1)
        for i in range(len(arr)-3,0,-1):
            arr[i] = arr[i+1]
        return arr
if __name__ == '__main__':
    arr = [17,18,5,4,6,1]
    sol = Solution()
    print(sol.replaceElements(arr))
    print(sol.replaceElements2(arr))