
# O(N) - solution
def solution(A):
    # len(A)+2 for the case that all values in A
    # are followers ( A[i-1] = A[i] or A[i] + 1
    values = set(range(1, len(A) + 2))
    maxValue = 0
    for value in A:
        if value >= 0:
            if value > maxValue:
                maxValue = value
            if value in values:
                values.remove(value)
    # will return 1 if all values were negative
    return 1 if maxValue == 0 else min(values)

if __name__ == '__main__':
    A = [1, 3, 6, 4, 1, 2]
    B = [-1, -3]
    C = [1, 2, 3]
    D = [3,3,3]
    ans = solution(D)
    print(ans)
