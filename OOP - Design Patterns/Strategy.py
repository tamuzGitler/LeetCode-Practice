from abc import ABC, abstractmethod


class Strategy(ABC):
    @abstractmethod
    def attack(self):
        pass


class Fire(Strategy):
    def attack(self):
        print("shoot")


class DefaultMele(Strategy):
    def attack(self):
        print("mele attack")


class Arrow(Strategy):
    def attack(self):
        print("shoot arrow")


class Soldier:
    def __init__(self):
        self.soldier = DefaultMele()

    def setStrategy(self, name=None):
        if name == "fire":
            self.soldier = Fire()
        elif name == "arrow":
            self.soldier = Arrow()
        else:  # default
            self.soldier = DefaultMele()


if __name__ == '__main__':
    soldier = Soldier()
    soldier.soldier.attack()
    soldier.setStrategy("fire")
    soldier.soldier.attack()
    # soldier.setStrategy("arrow")
    # soldier.soldier.attack()
    # soldier.setStrategy()
    # soldier.soldier.attack()
