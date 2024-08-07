import random


def f5():
    return random.randrange(1, 6)


def f7():
    # sum can be in range 2-10
    while True:
        first = f5()
        second = f5()
        if first == 1 and second == 1:
            return 1
        elif first == 1 and second == 2:
            return 2
        elif first == 2 and second == 1:
            return 3
        elif first == 2 and second == 2:
            return 4
        elif first == 2 and second == 3:
            return 5
        elif first == 3 and second == 2:
            return 6
        elif first == 3 and second == 3:
            return 7


if __name__ == '__main__':
    print(f7())
    print(f7())
    print(f7())
    print(f7())
    print(f7())
    print(f7())
