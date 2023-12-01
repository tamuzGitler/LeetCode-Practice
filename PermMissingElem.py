

def solution(A):
    length = len(A) + 1
    a_sum = (length * (1 + length)) // 2
    for val in A:
        a_sum -= val
    return a_sum
if __name__ == '__main__':
    a_sum = solution([1,2,3,5,6,4])
    print(a_sum)