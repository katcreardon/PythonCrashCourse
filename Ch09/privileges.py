class User():
    """A model for a system user."""

    def __init__(self, first_name, last_name, age, gender):
        """Initialize attributes."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.age = age
        self.gender = gender
        self.name = self.first_name + ' ' + self.last_name
        self.login_attempts = 0


    def describe_user(self):
        print(self.name)
        print("Age: " + str(self.age))
        print("Gender: " + self.gender)


    def greet_user(self):
        print("Hello, " + self.name + "!")


    def increment_login_attempts(self):
        self.login_attempts += 1


    def reset_login_attempts(self):
        self.login_attempts = 0


class Privileges():
    """Represents admin privileges."""
    def __init__(self, privileges=['can add post', 'can delete post', 'can ban user']):
        """Initialize the privilege's attributes."""
        self.privileges = privileges


    def show_privileges(self):
        """Print the admin's privileges."""
        for privilege in self.privileges:
            print(privilege)


class Admin(User):
    """Represents aspects of a user, specific to an admin."""

    def __init__(self, first_name, last_name, age, gender):
        """Initialize attributes of the parent class.
        Then initialize attributes specific to an admin."""
        super().__init__(first_name, last_name, age, gender)
        self.privileges = Privileges()


admin = Admin('adam', 'smith', 35, 'male')
admin.privileges.show_privileges()