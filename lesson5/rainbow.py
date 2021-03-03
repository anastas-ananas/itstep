rainbow_colours = ["Red", "Orange", "Yellow", "Green", "Blue", "Indigo", "Violet"]
user_input = input("Enter the colour of rainbow: ").capitalize()
if user_input in rainbow_colours:
    colour_index = rainbow_colours.index(user_input)
    if colour_index == 0:
        print(f"The next colour is {rainbow_colours[colour_index +1]}")
    elif colour_index == 6:
        print(f"the previous is {rainbow_colours[colour_index -1]}")
    else:
        print(f"The next colour is {rainbow_colours[colour_index +1]}, the previous is {rainbow_colours[colour_index -1]}")
