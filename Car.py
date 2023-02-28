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

    def fill_gas_tank(self):
        """Fill gas tank."""
        print("This car needs a gas tank!")

    def __repr__(self):
        return "Car('{}', '{}', {})".format(self.make, self.model, self.year)

    def __str__(self):
        return "Car's make is {}, model is {} and year is {}.".format(self.make, self.model, self.year)


class ElectricCar(Car):
    """
    Represent aspects of a car, specific to electric vehicles.

        Parameters: make (str): The make of the car.
                    model (str): The model of the car.
                    year (int): The year of the car.

        Returns: None

    """

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery() # Instance as attribute

    def fill_gas_tank(self):
        """Electric cars don't have gas tanks."""
        print("This car doesn't need a gas tank!")

    def __repr__(self):
        return "ElectricCar('{}', '{}', {})".format(self.make, self.model, self.year)

    def __str__(self):
        return "ElectricCar's make is {}, model is {} and year is {}.".format(self.make, self.model, self.year)


class Battery:
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=70):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print("This car has a {}-kWh battery.".format(self.battery_size))

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = "This car can go approximately {} miles on a full charge.".format(range)
        print(message)

    def upgrade_battery(self):
        """Upgrade the battery if possible."""
        if self.battery_size != 85:
            self.battery_size = 85


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
electric_car = ElectricCar('tesla', 'model s', 2016)
print(repr(electric_car))
print(str(electric_car))
print(electric_car.get_descriptive_name())  # accessing parent class method
electric_car.battery.describe_battery() # accessing instance as attribute
electric_car.battery.get_range()
electric_car.battery.upgrade_battery()
electric_car.battery.describe_battery()
my_new_car.fill_gas_tank()
electric_car.fill_gas_tank()  # overriding parent class method
