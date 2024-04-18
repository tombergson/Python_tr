current_users = ['jan', 'adam', 'ewa', 'kasia', 'marek']
new_users = ['KasiA', 'Marek', 'Tomek', 'Monika', 'Ewa', 'eryk']

for user in new_users:
    if user.lower() in current_users:
        print(f"{user} jest już w użyciu. Wybierz inną nazwę.")
    else:
        print(f"{user} jest dostępny.")
