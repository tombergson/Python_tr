#Program w Pythonie obliczający cenę biletu do kina (petla while):


while True:
  wiek = int(input("Podaj swój wiek: "))

  if wiek < 3:
    cena = 0
    komunikat = "Bilet jest bezpłatny!"
  elif wiek <= 12:
    cena = 10
    komunikat = "Cena biletu to 10 zł."
  else:
    cena = 15
    komunikat = "Cena biletu to 15 zł."

  print(komunikat)

  # Opcjonalne: zapytaj użytkownika, czy chce sprawdzić cenę dla innego wieku
  odpowiedz = input("Czy chcesz sprawdzić cenę dla innego wieku? (tak/nie) ")
  if odpowiedz.lower() == "nie":
    break
