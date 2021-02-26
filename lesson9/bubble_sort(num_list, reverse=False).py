def bubble_sort(num_list, reverse=False):
    result_list = []
    result_list.extend(num_list)
    list_size = len(result_list)

    # Проходимся по всьому списку.
    # З кожною наступною ітерацією більще число стає в кінець
    for counter in range(list_size):
        # Позиція останнього невідсортованого числа
        last_num_pos = list_size - 1 - counter

        # Ще не відсортовані числа
        sort_elements = range(0, last_num_pos)

        for num in sort_elements:
            if reverse:
                # Якщо перше число менше, ніж друге:
                if result_list[num] < result_list[num + 1]:
                    # змінюємо позиції елементів однією операцією:
                    result_list[num], result_list[num + 1] = result_list[num + 1], result_list[num]
            else:
                # Якщо перше число більше, ніж друге:
                if result_list[num] > result_list[num + 1]:
                    # змінюємо позиції елементів однією операцією:
                    result_list[num], result_list[num + 1] = result_list[num + 1], result_list[num]

    return result_list


print(bubble_sort(num_list=[5, 8, 4, 2, 1]))


