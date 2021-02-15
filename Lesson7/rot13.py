user_input = input("Enter a text: ")
alphabet = "ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz"
result = ""

for character in user_input:
    character_position = (alphabet.find(character) + 26) % 52
    new_character = alphabet[character_position]
    result += result.join(new_character)

print(result)
