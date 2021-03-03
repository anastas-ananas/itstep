def triple_result(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs) * 3
    return wrapper


@triple_result
def add(a, b):
    return a + b


print(add(5, 5))
