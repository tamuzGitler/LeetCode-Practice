# O(root of N)
import math


def solution(N):
    counter = 0  # count N
    i = 1
    while (i * i < N):
        if N % i == 0:
            counter += 2
        i += 1
    if i * i == N:  # check root
        counter += 1
    return counter


if __name__ == '__main__':
    N = 17
    counter = solution(N)
    print(counter)
