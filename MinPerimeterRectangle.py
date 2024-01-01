import math


def solution(N):
    # Implement your solution here
    divs = []
    for i in range(1,round(math.sqrt(N))  + 1):
        if N % i == 0:
            divs.append((i,N/i))
    min_perimeter = 2*(divs[0][0] + divs[0][1])
    for i in range(1,len(divs)):
        min_perimeter = min(2*(divs[i][0] + divs[i][1]), min_perimeter)


    return min_perimeter

if __name__ == '__main__':
    perimeter = solution(N=30)
    print(perimeter)