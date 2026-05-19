from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name):
        self.name = name
    
    @abstractmethod
    def speak(self):
        pass 

    @abstractmethod
    def movement(self):
        pass

class Dog(Animal):  # Subclass of Animal.
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def speak(self):  # Implements speak.
        return "Woof!"
    
    def movement(self):  # Implements movement.
        return "Run"

class Cat(Animal):  # Subclass of Animal.
    def speak(self):  # Implements speak.
        return "Meow!"
    
    def movement(self):  # Implements movement.
        return "Sneak"

animals = [Dog("Fido", "Labrador"), Cat("Misty")]

for animal in animals:
   print(f"{animal.name} says: {animal.speak()} "
         f"movement: {animal.movement()}")

another_animal = Animal("ImpossibleAnimal")
another_animal.speak()
