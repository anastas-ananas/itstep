def only_odd_arguments(func):
    def wrapper(*args, **kwargs):
        for number in args:
            if number % 2 == 0:
                print("Please, add odd numbers!")
                return
            else:
                return func(*args, **kwargs)

    return wrapper


@only_odd_arguments
def add(a, b):
    return a + b


@only_odd_arguments
def multiply(a, b, c, d, e):
    return a * b * c * d * e
