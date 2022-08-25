def cookbook():
    cook_book = {}
    foods = []
    j = 0
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
            j = read_book[i + 2 + k]
            cook_book[read_book[i]].append({j})

    return cook_book


print(cookbook())
