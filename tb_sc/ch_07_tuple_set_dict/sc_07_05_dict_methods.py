# file: ch_07_tuple_set_dict/sc_07_05_dict_methods.py
# Demonstration of various dictionary methods in Python

license_registry = {
    "AB-12345": "Alice Johnson",
    "CD-67890": "Bob Smith",
    "EF-54321": "Charlie Brown"
}

# pop() - Fjerner og returnerer verdien for en nøkkel
print("\n--- pop(): Remove and return value for a key ---")
print(f"Original: {license_registry}")
removed_driver = license_registry.pop("AB-12345")
print(f"Removed driver: {removed_driver}")
print(f"After pop: {license_registry}")

# popitem() - Fjerner og returnerer siste (nøkkel, verdi) par
print("\n--- popitem(): Remove and return last (key, value) pair ---")
license_registry = {
    "AB-12345": "Alice Johnson",
    "CD-67890": "Bob Smith",
    "EF-54321": "Charlie Brown"
}
print(f"Original: {license_registry}")
last_license, last_driver = license_registry.popitem()
print(f"Removed: {last_license} -> {last_driver}")
print(f"After popitem: {license_registry}")

# fromkeys() - Lager ny dict med samme nøkler og standardverdi
print("\n--- fromkeys(): Create new dict with keys and default value ---")
license_keys = ["AB-12345", "CD-67890", "EF-54321"]
inactive_licenses = dict.fromkeys(license_keys, "INACTIVE")
print(f"Created from keys: {inactive_licenses}")

# setdefault() - Henter verdi eller setter default hvis nøkkel mangler
print("\n--- setdefault(): Get value or set default if key missing ---")
license_registry = {
    "AB-12345": "Alice Johnson",
    "CD-67890": "Bob Smith"
}
print(f"Original: {license_registry}")
# Nøkkel finnes - returnerer eksisterende verdi
existing = license_registry.setdefault("AB-12345", "Unknown")
print(f"Key exists, returned: {existing}")
# Nøkkel finnes ikke - setter og returnerer default
new_entry = license_registry.setdefault("EF-54321", "Charlie Brown")
print(f"Key missing, set and returned: {new_entry}")
print(f"After setdefault: {license_registry}")

# copy() - Lager en uavhengig kopi av dicten
print("\n--- copy(): Create independent copy ---")
license_registry = {
    "AB-12345": "Alice Johnson",
    "CD-67890": "Bob Smith",
    "EF-54321": "Charlie Brown"
}
print(f"Original: {license_registry}")
backup_registry = license_registry.copy()
backup_registry["AB-12345"] = "Alice Smith"  # Endrer kopien
print(f"After modifying copy: {license_registry}")
print(f"Modified copy: {backup_registry}")

# merge (|) - Kombinerer to dicts (Python 3.9+)
print("\n--- Merge (|): Combine two dicts ---")
license_registry = {
    "AB-12345": "Alice Johnson",
    "CD-67890": "Bob Smith"
}
new_licenses = {
    "GH-11111": "David Lee",
    "IJ-22222": "Eve Wilson"
}
print(f"Original: {license_registry}")
print(f"New licenses: {new_licenses}")
merged = license_registry | new_licenses
print(f"Merged: {merged}")

# update() - Oppdaterer dict med nøkler fra annen dict
print("\n--- update(): Update dict with another dict ---")
license_registry = {
    "AB-12345": "Alice Johnson",
    "CD-67890": "Bob Smith"
}
print(f"Before update: {license_registry}")
license_registry.update({"AB-12345": "Alice A. Johnson", "EF-54321": "Charlie Brown"})
print(f"After update: {license_registry}")

# clear() - Tømmer hele dicten
print("\n--- clear(): Empty the entire dict ---")
temporary_registry = {"XY-99999": "Temporary Driver"}
print(f"Before clear: {temporary_registry}")
temporary_registry.clear()
print(f"After clear: {temporary_registry}")