# O(N) solution
def solution(N, A):
    counters = [0] * N
    maxCounter = 0
    increaseToMax = 0
    for index in A:
        # check if index is in valid range
        if 1 <= index <= N:
            index = index - 1
            counters[index] = max(maxCounter, counters[index])
            counters[index] += 1
            increaseToMax = max(increaseToMax, counters[index])  # keep track of the maximum value in counters
        # index is invalid range - all counters are set to the maximum value of any counter.
        else:
            maxCounter = increaseToMax

    for i in range(N):
        counters[i] = max(maxCounter, counters[i])  # set counters that are less the maxCounter to maxCounter
    return counters


if __name__ == '__main__':
    N = 5
    A = [3, 4, 4, 6, 1, 4, 4]
    counters = solution(N, A)

