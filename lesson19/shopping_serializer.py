import json
import pickle

shopping_list_example = [
    {
        "bread": 1.2,
        "milk": 1.6,
        "potato": 0.4,
        "sunflower oil": 2,
        "meat": 2.4
    },
    {
        "bread": 1.2,
        "milk": 1.6,
        "potato": 0.4,
        "sunflower oil": 2,
        "meat": 2.4

    }
]


#pickle
with open("shopping_list.pkl", 'wb') as f:
    pickle.dump(shopping_list_example, f)

with open("shopping_list.pkl", 'rb') as f:
    new_shopping_list = pickle.load(f)

print(new_shopping_list)

#json

with open("shopping_list.json", "w") as f2:
    json.dump(shopping_list_example, f2)

with open('shopping_list.json', 'r') as f2:
    new_shopping_list_json = json.load(f2) #загнали все, что получилось в переменную
print(new_shopping_list_json)

