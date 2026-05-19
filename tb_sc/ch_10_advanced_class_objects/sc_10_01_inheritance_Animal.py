# file: sc_10_01_inheritance_Animal.py
class Animal:  # Parent class, inherits from object.
    def __init__(self, name):
        self._name = name

    def speak(self):
        return "Some generic animal sound"

class Dog(Animal):  # Subclass of Animal.
    def __init__(self, name, breed):
        super().__init__(name)  # Call the parent class __init__.
        self.breed = breed

    def speak(self):  # Overrides speak from Animal.
        return "Woof!"

class Cat(Animal):  # Subclass of Animal.
    def speak(self):  # Overrides speak from Animal.
        return "Meow!"

# Polymorphism in practice:
animals = [Dog("Fido", "Labrador"), Cat("Misty"), Animal("Generic")]

for animal in animals:
   print(f"{animal._name} says: {animal.speak()}")
