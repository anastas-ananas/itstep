result = []

for number in range(2, 300):
    for i in range(2, number):
        if number % i == 0:
            break
    else:
        result.append(number)
    if len(result) == 42:
        break

print(result)
print(f"Number of digits: {len(result)}")
