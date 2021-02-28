from lesson10.even_list_generate import even_list_generate


def every_third(num1, num2):
    return even_list_generate(num1, num2)[2:: 3]


print(every_third(10, 50))


