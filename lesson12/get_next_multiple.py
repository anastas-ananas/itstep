def get_next_multiple(number):
    for i in range(1, 100):
        yield i * number


get_multiple_of_two = get_next_multiple(13)
print(next(get_multiple_of_two))
print(next(get_multiple_of_two))
print(next(get_multiple_of_two))
print(next(get_multiple_of_two))
print(next(get_multiple_of_two))
print(next(get_multiple_of_two))

