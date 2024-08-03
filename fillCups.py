import heapq


class Solution(object):
    def fillCups(self, amount):
        """
        :type amount: List[int]
        :rtype: int
        """
        seconds = 0
        if sum(amount) == 0:
            return seconds
        heap = [-val for val in amount]
        heapq.heapify(heap)

        while heap:
            if len(heap) >= 2:
                first = -heapq.heappop(heap)
                second = -heapq.heappop(heap)
                first -= 1
                second -= 1
                if first > 0:
                    heapq.heappush(heap, -first)
                if second > 0:
                    heapq.heappush(heap, -second)
                seconds += 1
            else:
                seconds += -heapq.heappop(heap)
                break
        return seconds


if __name__ == '__main__':
    amount = [0, 0, 0]
    sol = Solution()
    print(sol.fillCups(amount))
