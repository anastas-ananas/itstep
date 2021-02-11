values = []
for counter in range(0, 500):
    if counter % 5 == 0:
        values.append(counter)
    if len(values) == 30:
        break
print(values)
print(len(values))