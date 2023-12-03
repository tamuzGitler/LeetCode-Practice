# O(B-A) brut solution
def solution1(A, B, K):
    # Implement your solution here
    counter = 0
    for i in range(A,B+1):
        if i % K == 0:
            counter += 1
    return counter

# O(1) solution
def solution2(A, B, K):
    divisibles = (B // K)- (A // K) # number of divisibles between [A,B]
    if A % K == 0: # special case
        divisibles +=1
    return divisibles

if __name__ == '__main__':
    A,B,K = 6, 11,2
    print(solution2(A,B,K))