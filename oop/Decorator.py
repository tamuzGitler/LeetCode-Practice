def upperCaseDecorator(func):
    def wrapper(txt):
        result = func(txt)
        return result.upper()

    return wrapper


@upperCaseDecorator
def baseDecorator(txt):
    return "recived txt was " + txt


if __name__ == '__main__':
    print(baseDecorator("tamuz"))
