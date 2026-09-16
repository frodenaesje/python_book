# file: snippet_dataclass_default_factory.py
# default_factory creates a fresh default value for each instance,
# so separate objects do not share the same mutable list.

from dataclasses import dataclass, field

@dataclass
class Bag:
    items: list = field(default_factory=list)

b1 = Bag()
b2 = Bag()
b1.items.append("apple")
print(b1.items)   # ['apple']
print(b2.items)   # []   - separate list, not shared
