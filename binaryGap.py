# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def solution(N):
    # Implement your solution here
    one_indexs = []
    longest_gap = 0
    binary_rep = get_binary_representation(N)
    print(binary_rep)
    binary_rep = str(binary_rep)
    for i in range(len(binary_rep)):
        # find the lowest index appearance of one in substring
        index = binary_rep.find('1', i, len(binary_rep))
        one_indexs.append(index)

    prev_index = one_indexs[0]
    for index in one_indexs[1:]:
        cur_gap = index - 1 - prev_index
        if cur_gap > longest_gap:
            longest_gap = cur_gap
        prev_index = index
    return longest_gap


def get_binary_representation(N):
    binary_rep = 0
    while (N != 0):
        i = 0
        while 2 ** (i + 1) <= N:
            i += 1
        cur_binary = 10 ** i
        binary_rep += cur_binary
        N = N - (2 ** i)
    return binary_rep


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(solution(555))
    print(solution(832))
    print(solution(1965))
    print(solution(1025))
