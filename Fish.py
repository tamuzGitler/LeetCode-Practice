def solution(A, B):
    # Implement your solution here
    fish_alive = len(A)
    downstream_stack = []
    for p in range(len(A)):
        if B[p] == 1:
            downstream_stack.append(A[p])
        else: # B[p] = 0
            while downstream_stack :
                if  downstream_stack[-1] > A[p]:
                    fish_alive -= 1
                    break
                else:
                    downstream_stack.pop()
                    fish_alive -= 1
    return fish_alive


if __name__ == '__main__':
    A = [4, 3, 2, 1, 5]
    # B = [0, 1, 0, 0, 0]
    B = [1, 0, 1, 1, 1]
    fish_alive = solution(A, B)
    print(fish_alive)
