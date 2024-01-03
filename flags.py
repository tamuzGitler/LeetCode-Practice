
def solution(A):
    # Implement your solution here
    max_flags = 0
    peaks = []
    for P in range(1,len(A)-1):
        if A[P-1] < A[P] > A[P+1]:
            peaks.append(P)
    if len(peaks) == 0 or len(peaks) == 1:
        return len(peaks)

    max_flags = round(len(A) ** 0.5 )#why? start with max and dicriment
    for i in range(min(len(peaks), max_flags + 1  )):
        prev = peaks[0]
        flags = max_flags -1
        for i in range(1,len(peaks)):
            if peaks[i] - prev >= max_flags:
                flags -= 1
                prev = peaks[i]
        if flags > 0:
            max_flags -= 1
        else:
            break

    return min(max_flags,len(peaks))




if __name__ == '__main__':
    A = [1,5,3,4,3,4,1,2,3,4,6,2]
    max_flags = solution(A)
    print(max_flags)
