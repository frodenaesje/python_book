# file: sc_10_15_abstractmethod.py
from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name):
        self._name = name

    @abstractmethod
    def speak(self):
        pass

    @abstractmethod
    def movement(self):
        pass

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self._breed = breed

    def speak(self):
        return "Woof!"

    def movement(self):
        return "Run"

class Cat(Animal):
    def speak(self):
        return "Meow!"

    def movement(self):
        return "Sneak"

animals = [Dog("Fido", "Labrador"), Cat("Misty")]
for animal in animals:
    print(f"{animal._name}: {animal.speak()}, {animal.movement()}")

animal = Animal("ImpossibleAnimal")   # Crashes!
