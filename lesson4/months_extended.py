#Тут я вирiшила доповнити завдання months. Я захотiла щоб мiй користувач вводив даннi до того моменту, поки сам не
#захоче вийти з программи, ввiвши значення exit. Попередження про те, що так можна закрити программу з'являться 1 раз
#пiсля першого виводу iнформацiї про мiсяць
show_hint = True
while True:
    user_input = input("Enter number from 1 to 12: ")
    if user_input == "1":
        print("January")
        if show_hint:
            print("Enter 'exit' if you want to quit")
            show_hint = False
    elif user_input == "2":
        print("February")
        if show_hint:
            print("Enter 'exit' if you want to quit")
            show_hint = False
    elif user_input == "3":
        print("March")
        if show_hint:
            print("Enter 'exit' if you want to quit")
            show_hint = False
    elif user_input == "4":
        print("April")
        if show_hint:
            print("Enter 'exit' if you want to quit")
            show_hint = False
    elif user_input == "5":
        print("May")
        if show_hint:
            print("Enter 'exit' if you want to quit")
            show_hint = False
    elif user_input == "6":
        print("June")
        if show_hint:
            print("Enter 'exit' if you want to quit")
            show_hint = False
    elif user_input == "7":
        print("July")
        if show_hint:
            print("Enter 'exit' if you want to quit")
            show_hint = False
    elif user_input == "8":
        print("August")
        if show_hint:
            print("Enter 'exit' if you want to quit")
            show_hint = False
    elif user_input == "9":
        print("September")
        if show_hint:
            print("Enter 'exit' if you want to quit")
            show_hint = False
    elif user_input == "10":
        print("October")
        if show_hint:
            print("Enter 'exit' if you want to quit")
            show_hint = False
    elif user_input == "11":
        print("November")
        if show_hint:
            print("Enter 'exit' if you want to quit")
            show_hint = False
    elif user_input == "12":
        print("December")
        if show_hint:
            print("Enter 'exit' if you want to quit")
            show_hint = False
    elif user_input == "exit":
        break
    else:
        print("You made a mistake, repeat with numbers from 1 to 12")
