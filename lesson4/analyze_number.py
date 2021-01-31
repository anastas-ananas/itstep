try:
    user_input = int(input("Enter your number, please "))
    if user_input % 2 == 0 and user_input > 0:
        print("this is even number, positive")
    elif user_input % 2 == 0 and user_input <0:
        print("This is even number, negative")
    elif not user_input %2 == 0 and user_input > 0:
        print("This is odd number, positive")
    elif user_input == 0:
        print("Not odd, not even number")
    else:
        print("This is odd number, negative")
except ValueError:
    print("Only digits allowed")