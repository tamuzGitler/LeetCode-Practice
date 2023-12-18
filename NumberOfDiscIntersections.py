# O(N^2) solution
def solution(A):
    # Implement your solution here
    circles = []
    count = 0
    for i in range(len(A)):
        circles.append((i - A[i], i + A[i]))
    print(circles)
    circles.sort()
    print(circles)
    for i, circle in enumerate(circles[0:-1]):
        s,e = circle
        for j, candidateCircle in enumerate(circles[i + 1:]):
            start, end = candidateCircle
            if e < start or s > end:
                continue
            count += 1
    return count


if __name__ == '__main__':
    A = [1, 5, 2, 1, 4, 0]
    count = solution(A)
    print(count)
