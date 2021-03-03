def find_all_entry(text, symbol):
    for item in text:
        if item == symbol:
            return text.index(item)


print(find_all_entry(text="find symbol", symbol="n"))


