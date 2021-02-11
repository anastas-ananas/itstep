try:
    user_input = int(input("Please, enter the digit from 1 to 10: "))
    counter = 1
    while counter <= 10:
        if 10 >= user_input >= 1:
            print(f"{user_input} * {counter} = {counter * user_input}")
        counter += 1
except ValueError:
    print("Only digits from 1 to 10 are allowed")

