def make_pizza(size, *toppings):
    """podsumowanie info o pizzy"""
    print(f"\nPrzygotowuję pizze o średnicy {size} cm, z nastepującymi dodatkami: ")
    for topping in toppings:
        print(f"- {topping}")