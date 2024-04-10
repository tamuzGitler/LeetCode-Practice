def test(*args, **kwargs):
    print(*args)
    print(kwargs)
    for arg in args:
        print(arg)
    for key in kwargs.keys():
        print(kwargs[key])

if __name__ == '__main__':
    test(4,5,4,5,num1=9,num2=8)
