def mex(arr):
    mexNum = 0
    s = set()
    ans = []
    for num in arr:
        s.add(num)
        while mexNum in s:
            mexNum += 1
        ans.append(mexNum)
    print(ans)


if __name__ == '__main__':
    arr = [1, 0, 5, 5, 3]
    mex(arr)
