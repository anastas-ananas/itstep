star = '*'
rows = 15
for row_counter in range(0, 15):
    spaces_amount = ' ' * (rows - row_counter - 1)
    star_amount = star * (2 * row_counter + 1)
    print(spaces_amount + star_amount)
