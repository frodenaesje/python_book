# File: sc_07_02_dict_demo.py
# Dictionary

# Motivation and use cases
# A dict can model related data about a real-world object.
person = {
    "name": "Anna",  # "name" is key, "Anna" is value
    "age": 30,       # "age" is key, 30 is value
    "town": "London" # "town" is key, "London" is value
}

# Basic operations
# Keys give meaningful lookup instead of numeric indexing.
license_registry = {
    "AB-12345": "Alice Johnson",
    "CD-67890": "Bob Smith",
    "EF-54321": "Charlie Brown"
}

# Retrieving values
# [] raises KeyError if missing; get() can return a default.
plate = "CD-67890"
owner = license_registry[plate]  # direct access
print(owner)
owner = license_registry.get(plate, "Unknown")  # default value returned if plate not found
print(owner)

# Adding and updating values
# Assignment adds a new key or updates an existing key.
license_registry["GH-11111"] = "Diana Prince"      # new element
license_registry["AB-12345"] = "Alice A. Johnson"  # update

# Removing values
# del removes by key; pop() removes and returns the value.
# Copies keep these examples independent when the whole file runs.
registry = license_registry.copy()
del registry["AB-12345"]

registry = license_registry.copy()
removed = registry.pop("AB-12345")

registry = license_registry.copy()
removed = registry.pop("AB-12345", "Unknown")  # no KeyError if missing

registry = license_registry.copy()
last_plate, last_owner = registry.popitem()
print(f"Removed: {last_plate} -> {last_owner}")


# Various useful methods
# fromkeys() creates a new dict from an iterable of keys.
license_keys = ["AB-12345", "CD-67890", "EF-54321"]
inactive = dict.fromkeys(license_keys, "INACTIVE")
# {"AB-12345": "INACTIVE", "CD-67890": "INACTIVE", ...}

# update() from another dict
license_registry.update({
    "AB-12345": "Alice A. Johnson",
    "EF-54321": "Charlie Brown"
})

# update() from list of tuples
license_registry.update([
    ("MN-44444", "Iris Chen"),
    ("OP-55555", "Jack Brown")
])

# update() from zip
plates = ["UV-88888", "WX-99999"]
owners = ["Maya Singh", "Noah Johnson"]
license_registry.update(zip(plates, owners))

# Merge dictionaries
new_licenses = {"YZ-00000": "Olivia Martinez"}
merged = license_registry | new_licenses  # makes a new dict
license_registry |= new_licenses          # updates in place

# setdefault()
existing = license_registry.setdefault("AB-12345", "Unknown")
new_entry = license_registry.setdefault("EF-54321", "Charlie Brown")


# Iterating over a dictionary - dictionary views
# Views are dynamic and reflect later changes to the dict.
for plate, owner in license_registry.items():
    print(f"{plate}: {owner}")

# Dictionary views
print(type(license_registry.keys()))    # <class 'dict_keys'>
print(type(license_registry.values()))  # <class 'dict_values'>
print(type(license_registry.items()))   # <class 'dict_items'>

keys_list = list(license_registry.keys())


# Sorting a dictionary
# dict has no sort() method; sorted() returns items in sorted order.
sorted_by_key = dict(sorted(license_registry.items()))
print(sorted_by_key)


def value_key(item):
    return item[1]  # item is a (key, value) tuple


sorted_by_value = dict(sorted(license_registry.items(), key=value_key))
print(sorted_by_value)

# get() supplies zero for unseen items so a dictionary can count occurrences.

# Count letters in a word
# get(letter, 0) starts unseen letters at zero.
word = "programming"
letter_count = {}

for letter in word:
    letter_count[letter] = letter_count.get(letter, 0) + 1

for letter, count in letter_count.items():
    print(f"'{letter}': {count}")


# Count words in a sentence
sentence = "the quick brown fox jumps over the lazy dog the fox is quick"
word_count = {}

for word in sentence.split():
    word_count[word] = word_count.get(word, 0) + 1

# Find the most common word
# key=word_count.get makes max() compare the counts.
most_common = max(word_count, key=word_count.get)
print(
    f"Most common word: '{most_common}' with "
    f"{word_count[most_common]} occurrences"
)
