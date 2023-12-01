# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def solution(A, K):
    # Implement your solution here
    array_length = len(A)
    if array_length == 0 or K == 0:
        return A
    K = K % array_length  # no reason to rotate more than needed
    end_of_array = A[array_length - K:]
    A[K:] = A[:array_length - K]
    A[:K] = end_of_array


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    A = [1, 2, 3, 4]
    K = 4
    solution(A, K)
    print(A)
