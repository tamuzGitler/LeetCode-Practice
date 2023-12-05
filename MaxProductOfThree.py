# brut force solution - O(N^3)
# my solution using sort - O(NlogN)
def solution(A):
    # Implement your solution here
    A.sort()  # O(NlogN)
    return max(A[-1] * A[-2] * A[-3], A[0] * A[1] * A[-1])

if __name__ == '__main__':
    A = [-3, 1, 2, -2, 5, 6]
    A = [-5, 5, -5, 4]
    # A = [-4, -6, 3, 4, 5]
    max_prod = solution(A)
    print(max_prod)
