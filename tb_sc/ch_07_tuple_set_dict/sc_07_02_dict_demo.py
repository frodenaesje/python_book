# File: sc_07_02_dict_demo.py
# Dictionary (dict) demonstration in Python

# Make a dict
word_list = {}
for word in ["dog", "cat", "dog"]:
    if word in word_list:
        word_list[word] = word_list[word] + 1
    else:
        word_list[word] = 1
print("Word counting:", word_list)

# Same result with get() - simpler code
word_list_get = {}
for word in ["dog", "cat", "dog"]:
    word_list_get[word] = word_list_get.get(word, 0) + 1
print("Word counting with get():", word_list_get)


# Example: License plate registry
license_registry = {
    "AB-12345": "Alice Johnson",
    "CD-67890": "Bob Smith",
    "EF-54321": "Charlie Brown"
}

# Lookup example
plate = "CD-67890"
owner = license_registry[plate]
print(f"Using []: License plate {plate} belongs to {owner}.")
owner = license_registry.get(plate, "Unknown owner")
print(f"Using get(): License plate {plate} belongs to {owner}.")
plate = "GH-11111" # Not in registry
owner = license_registry.get(plate, "Unknown owner")
print(f"Using get(): License plate {plate} belongs to {owner}.")

# Put a new entry into the dict
license_registry["GH-11111"] = "Diana Prince"

# Iterate through all keys and values
for key, value in license_registry.items():
    print(f"{key}: {value}")

# Iterate through keys only
for key in license_registry.keys():
    print(f"License plate: {key}")

# Iterate through values only
for value in license_registry.values():
    print(f"Owner: {value}")

keys_view = license_registry.keys()
values_view = license_registry.values()
items_view = license_registry.items()

print(type(keys_view))    # <class 'dict_keys'>
print(type(values_view))  # <class 'dict_values'>
print(type(items_view))   # <class 'dict_items'>

license_registry["IJ-22222"] = "Emma Wilson"
items_list = list(items_view)
print(items_list)


print("\n=== DIFFERENT WAYS TO ADD ENTRIES ===")

# Method 1: Bracket notation [] - already shown above
print(f"Current registry: {len(license_registry)} entries")

# Method 2: update() with dictionary
new_registrations = {"IJ-22223": "Paula Wilson", "KL-33333": "Frank Miller"}
license_registry.update(new_registrations)
print(f"After update(dict): {len(license_registry)} entries")

# Method 3: update() with list of tuples
license_registry.update([("MN-44444", "Iris Chen"), ("OP-55555", "Jack Brown")])
print(f"After update(tuples): {len(license_registry)} entries")

# Method 4: update() with list of lists
license_registry.update([["QR-66666", "Karen White"], ["ST-77777", "Leo Garcia"]])
print(f"After update(lists): {len(license_registry)} entries")

# Method 5: update() with zip
plates = ["UV-88888", "WX-99999"]
owners = ["Maya Singh", "Noah Johnson"]
license_registry.update(zip(plates, owners))
print(f"After update(zip): {len(license_registry)} entries")

# Method 6: update() with keyword arguments (demo with temp dict)
temp_registry = {}
temp_registry.update({"TMP-11111": "Test Owner 1"}, temp2="Test Owner 2", temp3="Test Owner 3")
print(f"Combined method demo: {temp_registry}")

# Method 7: setdefault() - only adds if key doesn't exist
license_registry.setdefault("AB-12345", "This won't replace Alice")
license_registry.setdefault("YZ-00000", "Olivia Martinez")
print(f"After setdefault(): {len(license_registry)} entries")

print("\n=== DIFFERENT WAYS TO DELETE ENTRIES ===")

# Method 1: del - removes key and raises KeyError if not found
del license_registry["YZ-00000"]
print(f"After del: {len(license_registry)} entries")

# Method 2: pop() - removes and returns value, raises KeyError if not found
owner = license_registry.pop("UV-88888")
print(f"Removed owner: {owner}")
print(f"After pop(): {len(license_registry)} entries")

# Method 3: pop() with default - returns default if key not found
owner = license_registry.pop("XX-99999", "Unknown")
print(f"pop() with default (non-existent key): {owner}")
print(f"After pop(default): {len(license_registry)} entries")

# Method 4: clear() - removes all entries
small_registry = {"TEST-1": "Test User 1", "TEST-2": "Test User 2"}
print(f"Small registry before clear(): {len(small_registry)} entries")
small_registry.clear()
print(f"Small registry after clear(): {len(small_registry)} entries")

print("\n=== FINAL REGISTRY ===")