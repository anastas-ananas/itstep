def even_list_generate(num1, num2):
    even_number_list = []
    # Try/except використовую для того, щоб программа не крашилась коли користувач вводить флоат і видала повідомлення,
    # що треба вводити тільки цілі числа
    try:
        for number in range(num1, num2 +1):
            if number < 0:
                print("Only whole numbers allowed")
                break
            elif number %2 == 0:
                even_number_list.append(number)
        return even_number_list
    except TypeError:
        print("Only whole numbers allowed")


print(even_list_generate(2, 22))

