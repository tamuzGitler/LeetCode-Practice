# naive solution - O(N^2) for each A[i] find matching pairs from index i+1..
def solution1(A):
    pairs = 0
    for i in range(len(A)):
        if not A[i]:  # traveling east
            for j in range(i + 1, len(A)):
                if A[j]:  # traveling west
                    pairs += 1
            if pairs > 1000000000:
                return -1
    return pairs

# O(N) solution, using prefix
def solution2(A):
    pairs = [0] * len(A)
    traveling_east = 0
    for i in range(len(A)):
        if not A[i]:
            traveling_east += 1
            pairs[i] = pairs[i-1]
        else:
            pairs[i] = traveling_east + pairs[i-1]
            if pairs[i] > 1000000000: # special return value as asked in the instructions
                return -1
    return pairs[-1]


if __name__ == '__main__':
    A = [0, 1, 0, 1, 1]
    ans = solution2(A)
    print(ans)
