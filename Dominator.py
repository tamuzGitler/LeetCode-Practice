
# O(NlogN) - naive solution, sort first
# O(N) - solution

def solution(A):
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
    return A.index(key_with_max_value) if counter[key_with_max_value] > len(A) / 2 else -1

if __name__ == '__main__':
    A = [12312,3,3,2,3,-1,3,3]
    A = []
    ans = solution(A)
    print(ans)