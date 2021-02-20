def num_len(number):
    count = 0
    while number > 0:
        number = number // 10
        count += 1
    return count


print(num_len(34567))




