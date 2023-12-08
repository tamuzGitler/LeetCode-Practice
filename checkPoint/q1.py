def solution(D, C, P):
    """
    this functions calculates the maximum total number of orders that can be fulfilled
    assume len(D) = len(C)
    :param D: delivery distance
    :param C: number of monitors to deliver
    :param P: supply
    :return: maximum total number of orders that can be fulfilled
    """
    total_orders = 0
    if P <= 0:  # check that monitors supply is greater than 0
        return total_orders
    distance_and_orders = list(zip(D, C))  # combine distance and order
    distance_and_orders.sort()  # by distance
    for distance, num_of_monitors in distance_and_orders:
        if P - num_of_monitors >= 0:  # check if the delivery of C[K] monitors can be fulfilled
            P = P - num_of_monitors  # update number of monitors left
            total_orders += 1
        else:
            break  # supply of monitors is over
    return total_orders


if __name__ == '__main__':
    # case 1
    D = [5, 11, 1, 3]
    C = [6, 1, 3, 2]
    P = 0
    # case 2
    # D = [10, 15, 1]
    # C = [10, 1, 2]
    # P = 3
    # case 3
    # D = [11, 18, 1]
    # C = [9, 18, 8]
    # P = 7
    # case 4
    # D = [1, 4, 2, 5]
    # C = [4, 9, 2, 3]
    # P = 19
    total_orders = solution(D, C, P)
    print(total_orders)
