try:
    number1 = int(input("Enter the first number: "))
    number2 = int(input("Enter the second number: "))
    if number1 == number2:
        print("EQUALS")
    else:
        if number1 > number2:
            print(f"{number1} {number2}")
        else:
            print(f"{number2} {number1}")
except ValueError:
    print("Am i a Joke to You?")
