class User:
    """
    A class that represents a user profile.

        Parameters: first_name (str): The first name of the user.
                    last_name (str): The last name of the user.
                    username (str): The username of the user.
                    email (str): The email of the user.
                    location (str): The location of the user.

        Returns: None

    """

    def __init__(self, first_name, last_name, username, email, location):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.location = location

    def describe_user(self):
        print("User's first name is {}.".format(self.first_name))
        print("User's last name is {}.".format(self.last_name))
        print("User's username is {}.".format(self.username))
        print("User's email is {}.".format(self.email))
        print("User's location is {}.".format(self.location))

    def greet_user(self):
        print("Hello {} {}, welcome back!".format(self.first_name, self.last_name))

    def __repr__(self):
        return "User('{}', '{}', '{}', '{}', '{}')".format(self.first_name, self.last_name, self.username, self.email,
                                                           self.location)

    def __str__(self):
        return "User's name is {} {}.".format(self.first_name, self.last_name)


user1 = User('Muhammad', 'Shahroz', 'mshahroz1996', 'shahrozarif28@gmail.com', 'Faisalabad')
print(repr(user1))
print(str(user1))
user1.describe_user()
user1.greet_user()
