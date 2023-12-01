# naive
def solution1(X, Y, D):
    steps = 0
    while (X < Y):
        X += D
        steps += 1
    return steps


# better
def solution2(X, Y, D):
    steps = ((Y - X) // D)
    if (Y - X) % D > 0:
        steps += 1
    return steps


if __name__ == '__main__':
    X, Y, D = 10, 100, 30
    print(solution1(X, Y, D) == solution2(X, Y, D))
