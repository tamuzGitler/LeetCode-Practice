# O(N) solution - create a set in range of needed leafs and iterate over array A until all of the leafs appeared.
def solution(X, A):
    # Implement your solution here
    all_positions = set(range(1,X+1))

    for i,val in enumerate(A):
        if val in all_positions:
            all_positions.remove(val)

        if not all_positions:
            return i
    return -1



if __name__ == '__main__':
    X,A = 5,[1,3,1,4,2,3,5,4]
    print(solution(X,A))