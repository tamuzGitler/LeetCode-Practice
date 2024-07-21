from abc import ABC, abstractmethod


class SingeltonPreson():
    _instance = None

    def __init__(self, name, age):
        if not SingeltonPreson._instance:
            self.name = name
            self.age = age
            SingeltonPreson._instance = self

    @staticmethod
    def getInstance():
        return SingeltonPreson._instance

    def print_data(self):
        print(SingeltonPreson._instance.name)


if __name__ == '__main__':
    print(5)
    s = SingeltonPreson("tamuz", 30)
    b = SingeltonPreson("sdf", 30)
    a = SingeltonPreson.getInstance()
