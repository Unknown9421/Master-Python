"""
    Learning About Python 3 Decorator
"""


def smart_calculator(function):

    # Inner function

    def inner(a, b):
        print(f"Iam going Divide {a} and {b}")
        if b == 0:
            print(f"Whoops! Can't Devide")
            return
        return function(a, b)

    return inner


@smart_calculator
def divine(a, b):
    print(f"Calculating...")
    return a/b


def work_for_all(func):

    def inner(*args, **kwargs):
        print(f"I can decorator any function")
        return func(*args, **kwargs)

    return inner


def star(func):
    def inner(*args, **kwargs):
        print("*" * 30)
        func(*args, **kwargs)
        print("*" * 30)
    return inner


def percent(func):
    def inner(*args, **kwargs):
        print("%" * 30)
        func(*args, **kwargs)
        print("%" * 30)
    return inner


@percent
@star
def printer(msg):
    print(msg)


printer("Hello")

