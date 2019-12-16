class Restaurant():
    """A model for a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize name and cuisine attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type


    def describe_restaurant(self):
        print(self.restaurant_name)
        print(self.cuisine_type)


    def open_restaurant(self):
        print("\nThe restaurant is open.")


restaurant = Restaurant("Elizabeth's Pizza", 'Italian')

print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant_2 = Restaurant('Sapporo', 'Japanese')
restaurant_3 = Restaurant('Hops', 'burgers')

restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()