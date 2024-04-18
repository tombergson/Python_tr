current_users = ['anna', 'jan', 'tomek', 'pawel', 'ola']

new_users = ['jan', 'marek', 'jorg', 'tim']


for new_user in new_users:
    if new_user.lower() in current_users:
        print(f"Przepraszam {new_user.title()}, ale ta nazwa jest zajeta!")
    
         
    else:
        print(f"Witaj, {new_user.title()} możesz uzyć tej nazwy!")