import math
from functools import reduce


def missingTwoNum(arr):
    arrProd = reduce((lambda x, y: x * y), arr)
    n = len(arr) + 2
    factorial = math.factorial(n)
    prod = factorial / arrProd
    sumN = (n * (n + 1)) / 2
    sumArr = sum(arr)
    x = -(sumN - sumArr)
    a = (-x + math.sqrt(x * x - 4 * prod)) / 2
    b = (-x - math.sqrt(x * x - 4 * prod)) / 2
    return (a, b)


if __name__ == '__main__':
    arr = [1, 3, 5]
    print(missingTwoNum(arr))
