import random


def findKthLargest(array, k):
    # find k largest element O(N)
    k = len(array) - k  # index of k in array

    def quickSelect(l, r):
        pivot, p = array[r], l  # most right element
        for i in range(l, r):
            if array[i] <= pivot:
                swap(i, p, array)
                p += 1
        swap(r, p, array)

        if k < p:
            return quickSelect(l, p - 1)
        elif k > p:
            return quickSelect(p + 1, r)
        elif k == p:
            return array[k]

    return quickSelect(0, len(array) - 1)


def swap(i, j, array):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp


if __name__ == '__main__':
    array = [3, 2, 1, 5, 6, 4]
    print(findKthLargest(array, 6))
