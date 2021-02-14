user_input = input("Enter a phrase: ").lower().replace(" ", "")
if user_input == user_input[:: -1]:
    print("It's a palindrome")
else:
    print("It's not a palindrome")

