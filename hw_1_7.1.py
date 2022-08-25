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


print(cookbook())

print(get_shop_list_by_dishes(['Омлет', 'Фахитос'], 3))
