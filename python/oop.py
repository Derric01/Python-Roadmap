# A class is like a blueprint for objects
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} says: Woof!")

# Creating an object (instance of Dog)
my_dog = Dog("Buddy", "Golden Retriever")
my_dog.bark()

print(f"My dog's name is {my_dog.name} and he is a {my_dog.breed}.")
