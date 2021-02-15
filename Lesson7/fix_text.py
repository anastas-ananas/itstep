user_input = input("Enter a text: ")
text = user_input.split(". ")
result = ""
counter = 0
for sentence in text:
    result += sentence.capitalize()
    if counter < len(text) - 1:
        result += ". "
    counter += 1
print(result)


