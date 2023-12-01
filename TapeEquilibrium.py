

# naive sol - O(N^2)
# iterate over the array O(N), for each elem calc the two sums O(N)

# O(N) sol, calc sums once and then iterate over array O(N) and use O(1) time complexity actions.
def solution(A):
    if not A:
        return 0
    leftSum = A[0]
    rightSum = sum(A[1:])
    minAbsDiff = abs(leftSum - rightSum)
    print(rightSum)
    for val in A[1:]:
        leftSum += val
        rightSum -= val
        curMinAbsDiff = abs(leftSum - rightSum)
        if curMinAbsDiff < minAbsDiff:
            minAbsDiff = curMinAbsDiff

    return minAbsDiff

if __name__ == '__main__':
    A = []
    minAbsDiff = solution(A)
    print(minAbsDiff)