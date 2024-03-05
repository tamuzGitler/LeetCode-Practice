import heapq


class Solution(object):
    def carPooling(self, trips, capacity):
        """
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool
        """
        minHeap = []
        # heapq.heapify(stack)
        trips.sort(key=lambda x: x[1])

        for trip in trips:

            while (minHeap and minHeap[0][0] <= trip[1]):
                capacity += minHeap[0][1]
                heapq.heappop(minHeap)
            numPassengers, end = trip[0], trip[2]
            if capacity >= numPassengers:
                capacity -= numPassengers
                heapq.heappush(minHeap, [end, numPassengers])
            else:
                return False
        return True


if __name__ == '__main__':
    # trips = [[2, 1, 5], [3, 3, 7]]
    # capacity = 4
    trips = [[3, 2, 8], [4, 4, 6], [10, 8, 9]]

    capacity = 11
    sol = Solution()
    print(sol.carPooling(trips, capacity))
