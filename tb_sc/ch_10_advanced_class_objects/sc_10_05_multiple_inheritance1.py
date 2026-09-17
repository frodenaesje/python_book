# file: sc_10_05_multiple_inheritance1.py
class Animal:
    def __init__(self, name):
        self._name = name

    def speak(self):
        return f"{self._name} makes a sound"

class Swimmer:
    def swim(self):
        return f"{self._name} is swimming"

class Flyer:
    def fly(self):
        return f"{self._name} is flying"

class Duck(Animal, Swimmer, Flyer):
    def __init__(self, name):
        Animal.__init__(self, name)

duck = Duck("Donald")
print(duck.speak())   # Donald makes a sound
print(duck.swim())    # Donald is swimming
print(duck.fly())     # Donald is flying
print(Duck.__mro__)