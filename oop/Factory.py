class Player:
    def __init__(self, lvl=0, weapon=None):
        self.lvl = lvl
        self.weapon = weapon


class Warrior(Player):
    def __init__(self, lvl=0, weapon=None):
        super().__init__(lvl, weapon)


class Magician(Player):
    def __init__(self, lvl=0, weapon=None):
        super().__init__(lvl, weapon)


class Factory:
    @staticmethod
    def getPlayer(name):
        if name == "warrior":
            return Warrior(10, "sword")
        elif name == "magician":
            return Warrior(8, "wand")
        else:
            return Player()


if __name__ == '__main__':
    w = Factory.getPlayer("warrior")
    m = Factory.getPlayer("magician")

    a = 5
