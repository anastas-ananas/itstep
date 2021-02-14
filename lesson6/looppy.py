result = []
for num in range(100, 0, -1):
    if num % 11 == 0 or num < 10:
        result.append(num)
print(result)
