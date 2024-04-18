class Car:
    """Prosta proba zaprezentowania samochodu"""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odo_reading = 0
    
    def get_discriptive_name(self):
        """Zwrot elegancko opisanego samochodu."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odo(self):
        """Wyswietla info o przebiegu samochodu"""
        print(f"Ten samochod ma przejechane {self.odo_reading} km.")

    def update_odo(self, mileage):
        """ Przypis. danej wartosci licznikowi przebiegu samochodu.
        Zmiana zostanie cofnieta w przypadku proby cofniecia licznika."""
        if mileage >= self.odo_reading:
            self.odo_reading = mileage
        else:
            print("Nie można cofnąc licznika!")

    def increment_odo(self, kilometers):
        """Inkrementacja wartosci licznika przebiegu samochodu o podana watrosc"""
        self.odo_reading += kilometers

class ElectricCar(Car):
    """Przedstawia cechy charakter. samochodu elektrycznego."""

    def __init__(self, make, model, year):
        """Inicjalizacja atrybutow klasy nadrzednej."""
        super().__init__(make, model, year)
        self.battery_size = 40 
    
    def describe_battery(self):
        """Wyswiewtla info o wielkosci akumulatora."""
        print(f"Ten samochod ma akumulator o pojemnnosci {self.battery_size} kWh.")



class Battery:
    """Prosta proba modelowania aku sam el."""

    def __init__(self, battery_size=40):
        """Inicjalizacja atrybutow aku."""
        self.battery_size = battery_size
    
    def describe_battery(self):
        """Wyswietlanie inf o wielkosci aku."""
        print(f"Ten samochod ma aku o pojrnmosci {self.battery_size} kWh.")
    
    def get_range(self):
        """wyswietla info o zasiegu"""
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 223
        print(f"Zasieg tego samochodu wynosi ok {range} km po pełnym naladowaniu")


class ElectricCar(Car):
    """Przedstawia cechy charakter. samochodu elektrycznego."""

    def __init__(self, make, model, year):
        """Inicjalizacja atrybutow klasy nadrzednej."""
        super().__init__(make, model, year)
        self.battery = Battery()
    
    
my_leaf = ElectricCar('nissan', 'leaf', 2022)
print(my_leaf.get_discriptive_name())
my_leaf.battery.describe_battery()
my_leaf.battery.get_range()

"""
my_leaf = ElectricCar('nissan', 'leaf', 2022)
print(my_leaf.get_discriptive_name())
my_leaf.describe_battery()

"""

"""page 225, 10.04.2024"""
    