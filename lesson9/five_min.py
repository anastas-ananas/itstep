def five_min(element1, element2, element3, element4, element5):
    lst = [element1, element2, element3, element4, element5]
    try:
        return min(lst)
    except TypeError:
        print("Only numbers or only strings are allowed")


print(five_min(1, 2, 3, 4, 5))


