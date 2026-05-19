# file: sc_08_13__dict_with_objects.py
class Person:
    def __init__(self, name, zipcode):
        self._name = name
        self._zipcode = zipcode

    @property
    def zipcode(self):
        return self._zipcode

    def __repr__(self):
        return f"{self._name}, {self._zipcode}"

data = {
    '01010112345': Person('Smith, John', '0101'),
    '02020223456': Person('Johnson, Mary', '0202'),
    '03030334567': Person('Williams, Peter', '0303'),
    '04040445678': Person('Brown, Anna', '0404')
}

def zipcode_key(item):
    return item[1].zipcode

# Sorting with function
sorted_by_zipcode = dict(sorted(data.items(), key=zipcode_key))

# Sorting with lambda
sorted_by_zipcode_lambda = dict(sorted(data.items(), key=lambda item: item[1].zipcode))

print("Sorted by zipcode (function):")
for ssn, person in sorted_by_zipcode.items():
    print(f"{ssn}: {person}")

print("\nSorted by zipcode (lambda):")
for ssn, person in sorted_by_zipcode_lambda.items():
    print(f"{ssn}: {person}")