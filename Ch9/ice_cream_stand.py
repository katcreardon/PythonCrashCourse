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


class IceCreamStand(Restaurant):
    """Represents aspects of a restaurant, specific to an ice cream stand."""

    def __init__(self, restaurant_name, cuisine_type, flavors):
        """Initialize attributes of the parent class.
        Then initialize attributes specific to an ice cream stand."""
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors


    def display_flavors(self):
        for flavor in self.flavors:
            print(flavor)


flavors = ['chocolate chip cookie dough', 'vanilla', 'chocolate', 'strawberry']
stand = IceCreamStand('Baskin Robbins', 'ice cream', flavors)
stand.display_flavors()