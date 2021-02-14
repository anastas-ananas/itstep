user_input = input("Enter a text: ")
count = 1
for words in user_input:
    if words in ('!', ",",  ";", ".", "-", "?", " "):
        count += 1
print(count)

