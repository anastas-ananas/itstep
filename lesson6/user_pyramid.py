star = '*'
try:
    rows = int(input("Enter  number of rows: "))
    for row_counter in range(0, rows):
        spaces_amount = ' ' * (rows - row_counter - 1)
        star_amount = star * (2 * row_counter + 1)
        print(spaces_amount + star_amount)
except ValueError:
    print("Only digits can be entered")