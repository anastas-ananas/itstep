try:
    the_first_number = int(input("Enter your number, please: "))
    math_action = input("Enter the sign (+, -, *, /) ")
    the_second_number = int(input("Enter the second digit, please: "))
    if math_action == "+":
        print(the_first_number + the_second_number)
    elif math_action == "-":
        print(the_first_number - the_second_number)
    elif math_action == "*":
        print(the_first_number * the_second_number)
    elif math_action == "/":
        print(the_first_number / the_second_number)
    else:
        print("Please, enter one of the signs: +, -, *, /")
except ValueError:
    print("Only digits alowed to do math actions")
