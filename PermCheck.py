# O(N) solution - create a set with permutation  
# iterate over array to check if all of the values in the permutation appears
def solution(A):
    permutation = set(range(1, len(A) + 1))
    for val in A:
        if val in permutation:
            permutation.remove(val)
    return 1 if not permutation else 0


if __name__ == '__main__':
    permutation = [4, 1, 3, 2]
    not_permutation = [4, 1, 3]
    print(solution(permutation))
    print(solution(not_permutation))
