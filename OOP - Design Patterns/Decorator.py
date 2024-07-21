from abc import ABC, abstractmethod
 

# pizza interface
class Pizza(ABC):
    @abstractmethod
    def getDescription(self):
        pass

    @abstractmethod
    def getCost(self):
        pass


# implement interface
class PlainPizza(Pizza):
    def getDescription(self):
        return "Dough"

    def getCost(self):
        return 4.5


# topping decorator
class ToppingDecorator(ABC):

    def __init__(self, pizza):
        self.pizza = pizza

    def getDescription(self):
        return self.pizza.getDescription()

    def getCost(self):
        return self.pizza.getCost()


# implement topping
class Mozarella(ToppingDecorator):
    def getDescription(self):
        return self.pizza.getDescription() + ", Mozarella"

    def getCost(self):
        return self.pizza.getCost() + 0.5


class TomatoSauce(ToppingDecorator):
    def getDescription(self):
        return self.pizza.getDescription() + ", Tomato sauce"

    def getCost(self):
        return self.pizza.getCost() + 1


class Olives(ToppingDecorator):
    def getDescription(self):
        return self.pizza.getDescription() + ", Olives"

    def getCost(self):
        return self.pizza.getCost() + 2


if __name__ == '__main__':
    # pizza = Olives(TomatoSauce(Mozarella(PlainPizza())))
    pizza = TomatoSauce(Mozarella(PlainPizza()))
    print(pizza.getDescription())
    print(pizza.getCost())
