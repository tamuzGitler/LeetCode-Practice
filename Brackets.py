
def solution(S):
    # Implement your solution here
    open = []
    openers = set(['{','[','('])
    for char in S:
        if char in openers:
            open.append(char)
        else:
            if not open:
                return 0
            last_opener = open.pop()
            if (char == ']' and last_opener != '[') or (char == '}' and last_opener != '{') or (char == ')' and last_opener != '('):
                return 0
    if open:
        return 0
    return 1
if __name__ == '__main__':
    S = '{[()()]}'
    S = '([)()]'
    print(solution(S))