try:
    user_input = int(input("Enter the number from 1 to 100: "))
    my_range = range(1, 101)
    if user_input not in my_range:
        print ("Please, enter the number from 1 to 100")
    elif user_input % 3 == 0 and user_input % 5 == 0:
        print("FizzBuzz")
    elif user_input % 3 == 0:
        print("Fizz")
    elif user_input % 5 == 0:
        print("Buzz")
    else:
        pass
except ValueError:
    print("Please, enter the number from 1 to 100")

