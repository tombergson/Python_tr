class Car:
    """Prosta próba zdefinowania samochodu"""

    def __init__(self, make, model, year):
        """inicjalizacja atrybutów opisujących samochód."""

        self.make = make
        self.model = model
        self. year = year
        self.odo_reading = 1212
    
    def get_discriptive_name(self):
        """Zwrot elegancko sformatowanego opisu samochodu"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odo(self):
        """wyswietla informacje o przebiegu samochodu"""
        print(f"Ten samochód ma przejechane {self.odo_reading} km.")

    def update_odo(self, mileage):

        if mileage >= self.odo_reading:
            self.odo_reading = mileage
        else:
            print("Nie można cofnąć licznika samochodu!")

    def increment_odo(self, kilometers):
        """Inkrementacja wartosci lincznika przebiegu o podana wartosc."""
        self.odo_reading += kilometers

my_used_car = Car('subaru', 'forester', 2020)
print(my_used_car.get_discriptive_name())

my_used_car.update_odo(23_000)
my_used_car.read_odo()

my_used_car.increment_odo(200)
my_used_car.read_odo()


"""my_new_car = Car('audi', 'a4', 2022)
print(my_new_car.get_discriptive_name())

my_new_car.update_odo(111)
my_new_car.read_odo()
"""
