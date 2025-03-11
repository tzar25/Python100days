def add(*args):
    return sum(a for a in args)


print(add(1, 2, 3))


def calculate(n, **kwargs):
    # for key, value in kwargs.items():
    #     print(f"key:{key}, value: {value}")
    n += kwargs['add']
    n *= kwargs['multiply']
    return n


print(calculate(7, add=3, multiply=5))
