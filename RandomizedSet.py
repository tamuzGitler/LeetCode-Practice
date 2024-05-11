import random


class RandomizedSet(object):

    def __init__(self):
        self.s = dict()

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.s:
            self.s[val] = True
            return True
        else:
            return False

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.s:
            del self.s[val]
            return True
        else:
            return False

    def getRandom(self):
        """
        :rtype: int
        """
        return random.choice(list(self.s.keys()))


# Your RandomizedSet object will be instantiated and called as such:
if __name__ == '__main__':
    val = 5
    obj = RandomizedSet()
    param_1 = obj.insert(val)
    param_1 = obj.insert(67)
    param_2 = obj.remove(val)
    param_3 = obj.getRandom()
