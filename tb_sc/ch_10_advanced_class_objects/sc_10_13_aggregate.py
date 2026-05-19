# file: sc_10_13_aggregate.py

class Person:
    def __init__(self, name):
        self._name = name

class Team:
    def __init__(self):
        self._members = []

    def add_member(self, person):
        self._members.append(person)

person1 = Person("Alice")
person2 = Person("Bob")

team = Team()
team.add_member(person1)
team.add_member(person2)
print("Team members:")
for member in team._members:
    print(member._name)
