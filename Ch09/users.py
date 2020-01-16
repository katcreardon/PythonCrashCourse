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


class Admin(User):
    """Represents aspects of a user, specific to an admin."""

    def __init__(self, first_name, last_name, age, gender, privileges):
        """Initialize attributes of the parent class.
        Then initialize attributes specific to an admin."""
        super().__init__(first_name, last_name, age, gender)
        self.privileges = privileges


    def show_privileges(self):
        for privilege in privileges:
            print(privilege)

user_1 = User('kathryn', 'reardon', 28, 'female')
user_2 = User('matt', 'lanouette', 31, 'male')
user_3 = User('jane', 'doe', 23, 'female')

user_1.describe_user()
user_1.greet_user()

user_2.describe_user()
user_2.greet_user()

user_3.describe_user()
user_3.greet_user()

user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()

print(user_1.login_attempts)
user_1.reset_login_attempts()
print(user_1.login_attempts)

privileges = ['can add post', 'can delete post', 'can ban user']
admin = Admin('adam', 'smith', 35, 'male', privileges)
admin.show_privileges()