def solution2(A):
    # Implement your solution here
    if not A:
        return -1
    counter = dict()
    for val in A:
        if val not in counter.keys():
            counter[val] = 1
        else:
            counter[val] += 1
    key_with_max_value = max(counter, key=counter.get)
    return (key_with_max_value) if counter[key_with_max_value] > len(A) / 2 else -1

def solutioin(A):
    key = solution2(A)
    occurrences = 0
    for val in A:
        if val == key:
            occurrences += 1
    c = [1] if A[0] == key else [0]
    for val in A[1:]:
        c.append(c[-1])
        if val == key:
            c[-1] += 1
    counter = 0
    for i in range(len(A)):
        left,right = c[i], occurrences - c[i]
        if i+1 < 2* l





if __name__ == '__main__':
    A = [4,3,4,4,4,2]
    print(solutioin(A))
