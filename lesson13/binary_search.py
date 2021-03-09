def find_num(lst, num):
    sorted_list = []
    sorted_list.extend(lst)
    sorted_list.sort()

    first_element = 0
    last_element = len(sorted_list) - 1
    mid_element = len(sorted_list) // 2

    while sorted_list[mid_element] != num and first_element <= last_element:
        # shift right
        if num > sorted_list[mid_element]:
            first_element = mid_element + 1
        # shift left
        else:
            last_element = mid_element - 1
        mid_element = (first_element + last_element) // 2

    return lst.index(sorted_list[mid_element])


print(find_num(lst=[2, 10, 14, 15, 22, 39, 48, 94, 65, 11], num=int(input("Enter a  number: "))))
