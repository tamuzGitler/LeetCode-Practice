def solution(H):
    min_num_of_blocks = 0
    # cur_height = H[0]
    stack = []
    for height in H:
        while (stack and height < stack[-1]):
            stack.pop()
        if stack and stack[-1] == height:
            continue
        else:
            min_num_of_blocks += 1
            stack.append(height)
    return min_num_of_blocks


if __name__ == '__main__':
    H = [8, 8, 5, 7, 9, 8, 7, 4, 8]

    print(solution(H))
