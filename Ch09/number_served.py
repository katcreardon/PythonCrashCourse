class Restaurant():
    """A model for a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize name and cuisine attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0


    def describe_restaurant(self):
        print(self.restaurant_name)
        print(self.cuisine_type)


    def open_restaurant(self):
        print("\nThe restaurant is open.")


    def set_number_served(self, number):
        self.number_served = number


    def increment_number_served(self, number):
        self.number_served += number

restaurant = Restaurant("Elizabeth's Pizza", 'Italian')

print(restaurant.number_served)

restaurant.number_served = 2
print(restaurant.number_served)

restaurant.set_number_served(5)
print(restaurant.number_served)

restaurant.increment_number_served(5)
print(restaurant.number_served)