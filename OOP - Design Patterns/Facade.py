class Flour:
    def createFlour(self):
        print("creating flour")


class Sauce:
    def createTomatoSauce(self):
        print("creating tomato sauce")

    def createCreamSauce(self):
        print("creating Cream sauce")


class Toppings:
    def addMushrom(self):
        print("adding mushroom topping")

    def addHam(self):
        print("adding ham topping")


class Oven:
    def cookPizza(self):
        print("cooking pizza 12 minutes")


class Chef:
    def __init__(self):
        # TODO: Notice the fields are private!
        self._flour = Flour()
        self._sauce = Sauce()
        self._toppings = Toppings()
        self._oven = Oven()

    def createPizza(self):
        self._flour.createFlour()
        self._sauce.createTomatoSauce()
        self._toppings.addHam()
        self._toppings.addMushrom()
        self._oven.cookPizza()


if __name__ == '__main__':
    chef = Chef()
    chef.createPizza()
