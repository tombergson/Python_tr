def make_sand(*toppings):
    print('\nPrzygotowuje kanapke z następującymi składnikami:')
    for topping in toppings:
        print(f"- {topping}")

make_sand('szynka')
make_sand('szynka', 'ser', 'salata')
make_sand('jojko', 'masło', 'ryba', 'ser')
