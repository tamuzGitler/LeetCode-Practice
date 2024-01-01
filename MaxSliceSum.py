# naive solution - O(N^2), 2 for loops, 1 for P 1 for Q
def solution2(A):
    max_sam = -float('inf')
    if len(A) == 1:
        return A[0]
    for P in range(len(A)):
        for Q in range(P, len(A)):
            cur_sum = sum(A[P:Q+1])
            if cur_sum > max_sam:
                max_sam = cur_sum
    return max_sam
# O(N) solution
def solution(A):
    max_sam = -float('inf')
    cur_sum = 0
    for val in A:
        cur_sum = max(val, val + cur_sum)
        max_sam = max(max_sam,cur_sum)
    return max_sam

if __name__ == '__main__':
    A = [3,2,-6,4,-2]
    # A = [-20,3,5]
    # A = [-11,-11,-11]
    # A = [-1,-10,-2]
    ans = solution(A)
    print(ans)