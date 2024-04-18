class Restaurant:
    """Klasa reprezentująca restaurację."""

    def __init__(self, restaurant_name, cousin_type):
        """Inicjalizacja atrybutów restauracji."""
        self.restaurant_name = restaurant_name  # Nazwa restauracji
        self.cousin_type = cousin_type  # Typ kuchni

    def describe_restaurant(self):
        """Opisuje restaurację."""
        print(f"Restauracja nazywa się {self.restaurant_name}. Jes to lokal typu {self.cousin_type}.")

    def open_restaurant(self):
        """Informuje o godzinach otwarcia."""
        print(f"Restauracja {self.restaurant_name} jest czynna w godzinach 10:00 - 22:00. ")

class IceCreamStand(Restaurant):
    """Klasa reprezentująca budkę z lodami (dziedzicząca po klasie Restaurant)."""

    def __init__(self, restaurant_name, cousin_type, flavours):
        """Inicjalizacja atrybutów budki z lodami."""
        self.flavours = flavours  # Lista smaków lodów
        super().__init__(restaurant_name, cousin_type)  # Wywołanie konstruktora klasy bazowej

    def describe_flavours(self):
        """Wyświetla dostępne smaki lodów."""
        print(f"W naszej restauracji {self.restaurant_name} zjesz lody o smaku: ")
        for flavour in self.flavours:
            print(f"- {flavour.title()}")

# Utworzenie egzemplarza budki z lodami
restaurant = IceCreamStand('Wenecja', 'pub', ['truskawka', 'mango', 'cytryna', 'wanilia'])

# Wywołanie metod
restaurant.describe_restaurant()  # Wyświetla informacje o restauracji
restaurant.open_restaurant()     # Wyświetla informacje o godzinach otwarcia
restaurant.describe_flavours()   # Wyświetla dostępne smaki lodów
