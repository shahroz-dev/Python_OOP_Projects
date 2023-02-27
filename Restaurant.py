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

    def describe_restaurant(self):
        print("Restaurant name is {} and cuisine type is {}.".format(self.restaurant_name, self.cuisine_type))

    def open_restaurant(self):
        print("Restaurant is open.")

    def __repr__(self):
        return "Restaurant('{}', '{}')".format(self.restaurant_name, self.cuisine_type)

    def __str__(self):
        return "Restaurant name is {} and cuisine type is {}.".format(self.restaurant_name, self.cuisine_type)


restaurant1 = Restaurant('KFC', 'Fast Food')
print(repr(restaurant1))
print(str(restaurant1))
restaurant1.describe_restaurant()
restaurant1.open_restaurant()
restaurant2 = Restaurant('McDonalds', 'Fast Food')
restaurant2.describe_restaurant()
restaurant3 = Restaurant('Burger King', 'Fast Food')
restaurant3.describe_restaurant()
