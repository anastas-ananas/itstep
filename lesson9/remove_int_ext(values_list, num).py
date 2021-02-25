def remove_int_ext(values_list, num):
    initial_size = len(values_list)
    for i in values_list:
        if num in values_list:
            values_list.remove(num)
    return initial_size - len(values_list)


print(remove_int_ext(values_list=[1, 2, 2, 2, 2, 3, 4, 4, ], num=2))
