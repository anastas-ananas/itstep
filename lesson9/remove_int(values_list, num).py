def remove_int(values_list, num):
    result = []
    result.extend(values_list)
    for i in values_list:
        if i == num:
            result.remove(i)
    return result


print(remove_int(values_list=[1, 2, 3, 4, 4], num=4))

