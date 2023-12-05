# O(N) time and space solution - convert the list into a set and return its length, used O(N) space
def solution(A):
    distinct_values = set(A) # convert a list into a set is O(N),
    return len(distinct_values)

# O(N) time, using O(N) space, without build in functions
def solution1(A):
    distinct = dict()
    for val in A:
        if val not in distinct:
            distinct[val] = 1
    return len(distinct.keys())

if __name__ == '__main__':
    A =[2,1,1,2,3,1,4,4,5,6,7,8]
    print(solution1(A))