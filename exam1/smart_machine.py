try:
    user_input = int(input("Enter a number: "))
    if user_input <= 100:
        print(user_input - 10)
    else:
        print(user_input - 20)
except ValueError:
    print("Enter the integer")


