class Item:
    # Class attribute (shared by all instances)
    store = "Walmart"

    # Constructor method, called when a new object is created
    def __init__(self, name, price):
        self.name = name  # Instance attribute
        self.price = price    # Instance attribute

    # Instance method
    def list(self):
        return f"Name:{self.name} Price:{self.price}"

    # Instance method
    def describe(self):
        return f"{self.name} is ${self.price} at {self.store}."

# Creating instances (objects) of the Dog class
Item1 = Item("Tank Top Shirt", 30)
Item2 = Item("Boots", 50)

# Calling methods to display items
print(Item1.list())
print(Item2.list())
# Call describe method to display Boots item
print(Item2.describe())