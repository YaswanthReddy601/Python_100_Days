
def add(*args):
    total = 0
    for x in args:
        total += x
    print(total)

add(1,2,3,4)

def calculate(**kwargs):
    print(kwargs["pen"])
    x = kwargs["pencil"]
    print(x)

calculate(pen = 5., pencil = 15)




