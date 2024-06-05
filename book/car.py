class Car:

    """Prosta proba zaprezentowania samochodu"""

    def __init__(self, make, model, year):
        """Inicjalizacja atrybutów opisujących samochód"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_discriptive_name(self):
        """Zwrot eleganco sformatowanego opisu"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """ Wyśiwetla info o przebiegu samochodu"""
        print(f"Ten samochód ma przejechne {self.odometer_reading} km.")

    def update_odometer(self):
        """Przypisanie wartosci licznikowi samochodu. zmiana zostanie odrzucona w przypadku próby cofnięcia"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("Nie można cofnąć licznika samochodu")
    
    def increment_odometer(self, kilometers):
        """Inkrementacja wartosci licznika o podaną wartość"""
        self.odometer_reading += kilometers
