from pprint import pprint


def dishes_positions(book):
    j = 0
    positions = []
    positions.append(j)
    for i in book:
        if i == '':
            positions.append(j + 1)
        j += 1
    return positions


def cookbook():
    cook_book = {}
    list_ingr = ['ingredient_name', 'quantity', 'measure']
    with open('recipes.txt', 'r') as f:
        read_book = f.read().splitlines()
    for i in dishes_positions(read_book):
        cook_book[read_book[i]] = []
        for k in range(0, int(read_book[i + 1])):
            ingredients = read_book[i + 2 + k].split(' | ')
            cook_book[read_book[i]].append({list_ingr[0]: ingredients[0],
                                            list_ingr[1]: int(ingredients[1]), list_ingr[2]: ingredients[2]})

    return cook_book


def get_shop_list_by_dishes(dishes, person_count):
    get_shop = {}
    for i in dishes:
        for j in cookbook()[i]:
            if j['ingredient_name'] not in get_shop:
                get_shop[j['ingredient_name']] = {'measure': j['measure'], 'quantity': j['quantity'] * person_count}
            else:
                get_shop[j['ingredient_name']]['quantity'] += j['quantity'] * person_count
    return get_shop


pprint(cookbook())

pprint(get_shop_list_by_dishes(['Омлет', 'Фахитос'], 3))
