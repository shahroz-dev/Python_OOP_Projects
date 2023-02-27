class Car:
    """
    A simple attempt to represent a car.

        Parameters: make (str): The make of the car.
                    model (str): The model of the car.
                    year (int): The year of the car.

        Returns: None
    """

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print("This car has {} miles on it.".format(self.odometer_reading))

    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles

    def __repr__(self):
        return "Car('{}', '{}', {})".format(self.make, self.model, self.year)

    def __str__(self):
        return "Car's make is {}, model is {} and year is {}.".format(self.make, self.model, self.year)


print(Car.__doc__)
my_new_car = Car('audi', 'a4', 2016)
print(repr(my_new_car))
print(str(my_new_car))
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
my_new_car.odometer_reading = 23
my_new_car.read_odometer()
my_new_car.update_odometer(22)
my_new_car.read_odometer()
my_new_car.update_odometer(24)
my_new_car.read_odometer()
my_new_car.increment_odometer(100)
my_new_car.read_odometer()