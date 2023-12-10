# O(NlogN) solution
def solution(A):
    # Implement your solution here
    A.sort()
    for i in range(len(A) - 2):
        a_p = A[i]
        a_q = A[i+1]
        a_r = A[i+2]
        if a_p + a_q > a_r and a_q + a_r > a_p and a_r + a_p > a_q:
            return 1
    return 0



if __name__ == '__main__':
    A = [10,2,5,1,8,20]
    A2 = [10,50,5,1]
    is_triangle = solution(A)
    print(is_triangle)