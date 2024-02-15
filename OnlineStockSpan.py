class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:

        span = 1
        while(self.stack and price >= self.stack[-1][0]):
            prevPrice, prevSpan = self.stack.pop()
            span += prevSpan

        self.stack.append([price, span])
        return self.stack[-1][1]


# Your StockSpanner object will be instantiated and called as such:
if __name__ == '__main__':
    obj = StockSpanner()
    print(obj.next(100))
    print(obj.next(80))
    print(obj.next(60))
    print(obj.next(70))
    print(obj.next(60))
    print(obj.next(75))
    print(obj.next(85))

