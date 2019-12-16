class User():
    """A model for a system user."""

    def __init__(self, first_name, last_name, age, gender):
        """Initialize attributes."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.age = age
        self.gender = gender
        self.name = self.first_name + ' ' + self.last_name


    def describe_user(self):
        print(self.name)
        print("Age: " + str(self.age))
        print("Gender: " + self.gender)


    def greet_user(self):
        print("Hello, " + self.name + "!")


user_1 = User('kathryn', 'reardon', 28, 'female')
user_2 = User('matt', 'lanouette', 31, 'male')
user_3 = User('jane', 'doe', 23, 'female')

user_1.describe_user()
user_1.greet_user()

user_2.describe_user()
user_2.greet_user()

user_3.describe_user()
user_3.greet_user()