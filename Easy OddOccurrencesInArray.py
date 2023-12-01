
def solution(A):
    # Implement your solution here
    apperances = dict()
    for num in A:
        if num in apperances:
            if apperances[num] == 2:
                continue
            apperances[num] += 1
        else:
            apperances[num] = 1

    for num in apperances.keys():
        if apperances[num] == 1:
            return num

def solution(A):
    appearance = set()
    for val in A:
        if val in appearance:
            appearance.remove(val)
        else:
            appearance.add(val)
    return appearance.pop()







if __name__ == '__main__':
    A = [9,3,9,3,9,1,9,10,8,10,8]
    num = solution2(A)
    print(num)