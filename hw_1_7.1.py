def cookbook():
    cook_book = {}
    foods = []
    j = 0
    list_ingr = ['ingredient_name', 'quantity', 'measure']
    with open('recipes.txt', 'r') as f:
        read_book = f.read().splitlines()
    foods.append(j)
    for i in read_book:
        if i == '':
            foods.append(j + 1)
        j += 1
    for i in foods:
        cook_book[read_book[i]] = []
        for k in range(0, int(read_book[i + 1])):
            ingredients = read_book[i + 2 + k].split(' | ')
            cook_book[read_book[i]].append(dict(zip(list_ingr, ingredients)))

    return cook_book


def get_shop_list_by_dishes(dishes, person_count):
    pass


get_shop_list_by_dishes(['Омлет', 'Фахитос'], 3)
