class Animal:
    def __init__(self, name):
        self.name = name
    
    def eat(self):
        return f"{self.name} is eating"
    
    def sleep(self):
        return f"{self.name} is sleeping"


class Dog(Animal)  :
    def bark(self):
        return f"{self.name} says woof!"


# Create a dog - using positional argument
my_dog = Dog("Buddy")
# Or with named argument
my_dog1 = Dog(name="Max")

# Dog can do animal things (inherited)
print(my_dog.eat())    # Buddy is eating
print(my_dog.sleep())  # Buddy is sleepin
# Dog can also do dog things
print(my_dog.bark())   # Buddy says woof!


