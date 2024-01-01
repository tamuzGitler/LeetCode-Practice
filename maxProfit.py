def solution(A):
    # start, end = 0, len(A) - 1
    # max_profit = max(0, A[end] - A[start])
    # while(start < end):
    #     if A[end-1] >= A[start]:
    #         end_profit = A[end-1] - A[start]
    #     else:
    #         end_profit = 0
    #     if A[end ] >= A[start+1]:
    #         start_proift = A[end ] - A[start+1]
    #     else:
    #         start_proift = 0
    #     if end_profit > start_proift:
    #         end = end - 1
    #         cur_profit = end_profit
    #     else:
    #         start = start + 1
    #         cur_profit = start_proift
    #
    #     max_profit = max(max_profit, cur_profit)
    #
    # return max_profit
    min_price_seen = float('inf')
    max_profit = 0
    for price in A:
        min_price_seen = min(min_price_seen, price)
        max_profit = max(max_profit, price - min_price_seen)
    return max_profit


if __name__ == '__main__':
    A = [23171,21011,21123,21366,21013,21367]
    # A = [100,120,80,101,142]
    max_profit = solution(A)
    print(max_profit)