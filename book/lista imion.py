names = ['eryk', 'wanda', 'ula', 'stefek', 'olek', 'marek']
new_u = ('ula', 'olek')

# Lista do przechowywania znalezionych imion
znalezione_imiona = []

# Iterowanie po liście names
for name in names:
    # Sprawdzanie, czy imię znajduje się w new_u
    if name in new_u:
        # Dodawanie znalezionego imienia do listy
        znalezione_imiona.append(name.title())

# Sprawdzenie, czy znaleziono imiona
if znalezione_imiona:
    # Połączenie imion z separatorem
    imiona_w_linii = ", ".join(znalezione_imiona)
    # Wyświetlenie imion w jednej linii
    print(imiona_w_linii)
else:
    # Komunikat o braku imion
    print("Nie znaleziono imion z listy new_u.")