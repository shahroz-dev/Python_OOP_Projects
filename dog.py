class Dog:
    """
    A simple attempt to model a dog.

        Parameters: name (str): The name of the dog.
                    age (int): The age of the dog.

        Returns: None
    """

    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print("{} is now sitting.".format(self.name.title()))

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print("{} rolled over!".format(self.name.title()))

    def __repr__(self):
        return "Dog('{}', {})".format(self.name, self.age)

    def __str__(self):
        return "Dog's name is {} and age is {}".format(self.name.title(), self.age)


print(Dog.__doc__)
my_dog = Dog('willie', 6)
print(repr(my_dog))
print(str(my_dog))
my_dog.sit()
my_dog.roll_over()
your_dog = Dog('lucy', 3)
print(repr(your_dog))
print(str(your_dog))
your_dog.sit()
your_dog.roll_over()
