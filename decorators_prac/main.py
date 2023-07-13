
def calculater(func):
    def wrapper(a,b):
        print(func(a,b))
        print(func(a,b)+200)
    return wrapper

@calculater
def sum(a, b):
    return a+b

sum(8,9)

@calculater
def mul(a,b):
    return a*b

mul(10, 20)


def sub(a, b):
    return a-b

calculate = calculater(sub)
calculate(100,10)