class Cashier(object):

    def __init__(self, n, discount, products, prices):
        """
        :type n: int
        :type discount: int
        :type products: List[int]
        :type prices: List[int]
        """
        self.n = n
        self.discount = discount
        self.products = products
        self.prices = prices
        self.custumers = 0
        self.lookup = dict()
        for product, price in zip(products, prices):
            self.lookup[product] = price

    def getBill(self, product, amount):
        """
        :type product: List[int]
        :type amount: List[int]
        :rtype: float
        """
        bill = 0
        self.custumers += 1

        for p, a in zip(product, amount):
            bill += a * self.lookup[p]
        if self.custumers % self.n == 0:
            bill = bill * ((100 - self.discount) / 100)
        return bill


# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product,amount)
if __name__ == '__main__':
    cashier = Cashier(3, 50, [1, 2, 3, 4, 5, 6, 7], [100, 200, 300, 400, 300, 200, 100])
    # print(cashier.getBill([1, 2], [1, 2]))
    print(cashier.getBill([3, 7], [10, 10]))
