import heapq


class SeatManager(object):

    def __init__(self, n):
        """
        :type n: int
        """
        self.seats = [*range(1, n+1, 1)]

    def reserve(self):
        """
        :rtype: int
        """
        return heapq.heappop(self.seats)

    def unreserve(self, seatNumber):
        """
        :type seatNumber: int
        :rtype: None
        """
        heapq.heappush(self.seats,seatNumber)

if __name__ == '__main__':
    n = 20
    seatNumber = 2
    obj = SeatManager(n)
    param_1 = obj.reserve()
    param_2 = obj.reserve()
    obj.unreserve(seatNumber)
    a=5
# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)