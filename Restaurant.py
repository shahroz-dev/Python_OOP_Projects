class Restaurant:
    """
    A simple attempt to model a restaurant.

        Parameter: restaurant_name (str): The name of the restaurant.
                      cuisine_type (str): The type of cuisine.

        Returns: None
    """

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print("Restaurant name is {} and cuisine type is {}.".format(self.restaurant_name, self.cuisine_type))

    def open_restaurant(self):
        print("Restaurant is open.")

    def restaurant_served(self):
        print("Restaurant has served {} customers.".format(self.number_served))

    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self, number_served):
        self.number_served += number_served

    def __repr__(self):
        return "Restaurant('{}', '{}')".format(self.restaurant_name, self.cuisine_type)

    def __str__(self):
        return "Restaurant name is {} and cuisine type is {}.".format(self.restaurant_name, self.cuisine_type)


class IceCreamStand(Restaurant):
    """
    A simple attempt to model an ice cream stand.

        Parameter: restaurant_name (str): The name of the restaurant.
                      cuisine_type (str): The type of cuisine.

        Returns: None
    """

    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['chocolate', 'vanilla', 'strawberry']

    def display_flavors(self):
        print("Ice cream flavors are: ")
        for flavor in self.flavors:
            print(flavor)

    def __repr__(self):
        return "IceCreamStand('{}', '{}')".format(self.restaurant_name, self.cuisine_type)

    def __str__(self):
        return "Ice cream stand name is {} and cuisine type is {}.".format(self.restaurant_name, self.cuisine_type)


print(Restaurant.__doc__)
restaurant1 = Restaurant('KFC', 'Fast Food')
print(repr(restaurant1))
print(str(restaurant1))
restaurant1.describe_restaurant()
restaurant1.open_restaurant()
restaurant2 = Restaurant('McDonalds', 'Fast Food')
restaurant2.describe_restaurant()
restaurant3 = Restaurant('Burger King', 'Fast Food')
restaurant3.describe_restaurant()
restaurant1.restaurant_served()
restaurant1.number_served = 10
restaurant1.restaurant_served()
restaurant1.set_number_served(20)
restaurant1.restaurant_served()
restaurant1.increment_number_served(10)
restaurant1.restaurant_served()
print(IceCreamStand.__doc__)
ice_cream_stand1 = IceCreamStand('Baskin Robbins', 'Ice Cream')
print(repr(ice_cream_stand1))
print(str(ice_cream_stand1))
ice_cream_stand1.describe_restaurant()
ice_cream_stand1.open_restaurant()
ice_cream_stand1.display_flavors()
