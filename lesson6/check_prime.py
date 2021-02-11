while True:
    try:
        user_input = int(input("Enter a number: "))
        if user_input > 1:
            for number in range(2, user_input):
                if (user_input % number) == 0:
                    print(user_input, "is not a prime number")
                    break
            else:
                print(user_input, "is a prime number")
                break
            break
        else:
            print(user_input, "is not a prime number")
            break
    except ValueError:
        print("Only numbers are allowed")
