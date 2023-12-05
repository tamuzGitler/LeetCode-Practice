def solution(A):
    ind = 0
    minSlice = (A[0] + A[1]) / 2.0  # Initialize to the average of the first two elements

    for i in range(2, len(A)):
        twoSliceAvg = (A[i-1] + A[i]) / 2.0
        threeSliceAvg = (A[i-2] + A[i-1] + A[i]) / 3.0
        cur_min_avg = min(twoSliceAvg,threeSliceAvg )

        if cur_min_avg < minSlice:
            minSlice = cur_min_avg
            ind = i - 1 if twoSliceAvg < threeSliceAvg else i - 2
    return ind

if __name__ == '__main__':
    A = [4,2,2,5,1,5,8]
    print(solution(A))
