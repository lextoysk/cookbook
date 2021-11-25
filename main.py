import os
path = f"{os.getcwd()}/recipes.txt"
with open(path, 'rt', encoding="utf-8") as file:
    print(file.read())
    result = {}
    name_dish = file.readline().strip()
    counter = int(file.readline().strip())

    for item in range(counter):
        temp_data = []
        ingredient_name, quantity, measure = file.readline().split(' | ')
        temp_data.append({'ingredient_name': ingredient_name, 'quantity': quantity,'measure': measure})
    result[name_dish] = temp_data


