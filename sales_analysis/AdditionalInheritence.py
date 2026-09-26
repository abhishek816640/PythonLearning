class Animal:
    def __init__(self,name):
        self.name = name
        self.ispet = True

    def AnimalStory(self):
         return f"{self.name} is loved by me"    

class Dog(Animal):
    def __init__(self,name,breed):
           super().__init__(name)
           self.breed = breed

    def describe(self):
         return f"{self.name} is a {self.breed}"

mydog1 = Dog("POM","labrador")
mydog2 = Dog(name="Max", breed="Poodle")

print(mydog1.describe())  # Buddy is a Golden Retriever
print(mydog1.ispet)
print(mydog1.AnimalStory())      # True (inherited from Animal)

    
                   