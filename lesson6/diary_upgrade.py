days_of_week = {
    "Monday": ["Call Andrew", "Do my homework"],
    "Tuesday": ["Clean my room"],
    "Wednesday": ["Go to walk", "Check my e-mail"],
    "Thursday": "",
    "Friday": ["Clean the kitchen", "Wash the dish"],
    "Saturday": ["Visit the doctor"],
    "Sunday": ["Go to church"]
}
show_hint = True
while True:
    user_input = input("Enter the day of the week: ").capitalize()
    if user_input.lower() == "exit":
        break
    if user_input in days_of_week:
        tasks = days_of_week.get(user_input)
        if tasks == "":
            print("You have no tasks for today")
        else:
            print(tasks)
    else:
        print("Please, enter the day of the week")
    if show_hint:
        print("Type 'exit' to quit")
        show_hint = False
