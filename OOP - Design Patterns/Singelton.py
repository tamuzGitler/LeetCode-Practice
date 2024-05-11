class A:
    staticField = 5

    def __init__(self):
        self.counter = 1


class Singelton:
    _instance = None

    # cls represents the class that is needed to be instantiated,
    # __new__ - automaticily static method
    def __new__(cls):
        if cls._instance is None:
            cls._instance = A()
        return cls._instance


if __name__ == '__main__':
    s = Singelton()
    a = Singelton()
    b = 5
