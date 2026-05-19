# file: sc_10_04_isinstance.py
class Animal:
    def speak(self):
        return "Some sound"

class Dog(Animal):
    def fetch(self):
        return "Fetching stick!"

class Cat(Animal):
    pass

animals = [Dog(), Cat(), Animal()]

for animal in animals:
    print(animal.speak())
    if isinstance(animal, Dog):
        print(animal.fetch())  # Only Dog has the fetch method.
