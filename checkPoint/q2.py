# first approach - O(NlogN) time (sort), and O(N) space complexity
def solution(A):
    min_num_of_room_needed = 0
    demands = set()
    A.sort()
    for guestDemand in A:
        demands.add(guestDemand)
        demands = {demand - 1 for demand in demands}

        if 0 in demands:
            min_num_of_room_needed += 1
            demands.clear()
    if len(demands):
        min_num_of_room_needed += 1
    return min_num_of_room_needed


# second approach - O(NlogN) time (reverse sort) and O(1) space complexity
def solution2(A):
    A.sort(reverse=True)
    min_num_of_room_needed = 0
    room_capacity = 0
    for guestDemand in A:
        if guestDemand <= room_capacity:
            min_num_of_room_needed += 1
            room_capacity = 1
        else:
            room_capacity += 1
    if room_capacity >= 1:
        min_num_of_room_needed += 1
    return min_num_of_room_needed


if __name__ == '__main__':
    # case 1
    A = [1,1,1,1,1] # 5
    #
    # # case 2
    # A = [2,1,4]  # 2
    #
    # # case 3
    # A = [2, 7, 2, 9, 8]  # 2
    #
    # # case 4
    # A = [7, 3, 1, 1, 4, 5, 4, 9]  # 4
    min_num_of_room_needed = solution2(A)
    print(min_num_of_room_needed)
