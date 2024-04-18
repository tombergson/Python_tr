def print_models(unprinted_designs, completed_models):
    """
    symulujemy wydruk poszczegolnych projektow, dopoki pozostal jakikolwiek
    projekt na liscie
    """

    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Wydruk modelu {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """wyswietla wszystke modele, ktore zostaly wydrukowane"""
    print("\nWydrukowane zostały nastepujace modele:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['etui', 'pudelko', 'pilot']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

#Page 195