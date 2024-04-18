"""age = int(input("Wpisz wiek: ")) 
if age <= 4:
    print("Wchodzisz za darmo!")
elif age < 18:
    print("Cena biletu 20 zł.")
else:
    print("Cena biletu 40 zł.")"""

age = int(input("Wpisz wiek: "))

if age <= 4:
    price = 0
elif age < 18:
    price = 20
elif age > 65:
    price = 30
else:
    price = 40

print(f"Cena biletu wynosi {price} zł.")