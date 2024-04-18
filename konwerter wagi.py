weight = int(input("Waga: "))
unit = input("K(g) or (L)bs: ")
if unit.upper() == "K":
    converted = weight / 0.45
    print("Waga w Lbs: " + str(converted))
else:
    converted = weight * 0.45
    print("Waga w Kg: " + str(converted))