import os.path
check_file = os.path.exists('mycookbook.txt')
if check_file == False:
    file = open('mycookbook.txt', 'tw', encoding='utf-8')
    file.close()

def main_commands():
    print('\n- Основные команды ___ main')
    print('- Добавление рецепта ___ add')
    print('- Вывести список рецептов___ list')
    print('- Расчет требуемых ингридиентов для приготовления блюд___ count')
    print('- Выход из программы___ end')

def new_recipe():
    with open('mycookbook.txt', 'a+') as myfile:
        newrecipe = input('Введите название блюда ___ ')
        myfile.write('\n' + newrecipe)
        numbering = input("Введите количество ингридиентов ")
        myfile.write('\n' + numbering)
        myfile.write('\n')
        number = 0
        while number < int(numbering):
            ingredient_name = input('Название ингридиента ')
            quantity = input('Количество ')
            measure = input('Мера ')
            number = number+1
            myfile.write(ingredient_name + '|' + quantity + '|' + measure + '\n')
    main_commands()

def read_cookbook():
    with open('mycookbook.txt', 'r') as myfile:
        while True:
            line = myfile.readline()
            if not line:
                break
            print(line.strip())

def cook_bookdic():
    st_tit = 1
    st_count = 2
    st_ingred = 3
    state = st_tit
    with open("mycookbook.txt", 'r') as myfile:
        for line in myfile:
            line = line.strip()
            if not line: continue
            if state == st_tit:
                title = line
                cook_book[title] = []
                state = st_count
            elif state == st_count:
                count = int(line)
                state = st_ingred
            else:
                data = [x.strip() for x in line.split('|')]
                data[1] = int(data[1])
                cook_book[title].append(dict(zip(('ingredient_name', 'quantity', 'measure'), data)))
                count -= 1
                if count == 0:
                    state = st_tit

def create_shop_list():
    cook_bookdic()
    person_count = int(input('Введите нужное количество человек: '))
    dishes = input('Введите требуемые блюда в расчете на одного человека (через запятую): ').split(', ')
    print()
    get_shop_list_by_dishes(dishes, person_count)

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    shop_listingred = {}
    for item in dishes:
        for key, vol in cook_book.items():
            if key == item:
                shop_list.update({key: vol})
    for keys, values in shop_list.items():
        for step1 in values:
            new_quantity = (step1['quantity'])*person_count
            step1.update({'quantity': new_quantity})
    for keys1, items1 in shop_list.items():
        for keys2 in items1:
            shop_listingred.update({'measure': keys2['measure'], 'quantity': keys2['quantity']})
            print(f"'{keys2['ingredient_name']}': {shop_listingred}")

main_commands()
cook_book = {}
while True:
    command = input('- Введите команду (команды/main__добавить/add__вывод/list__расчет/count__выход/end): ')
    if command == 'main':
        main_commands()
    if command == 'list':
        read_cookbook()
    if command == 'add':
        new_recipe()
    if command == 'count':
        create_shop_list()
    if command == 'dic':
        cook_bookdic()
    if command == 'end':
        break
