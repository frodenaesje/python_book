def natural_enumeration(items: list) -> str:
    if not items:
        return ""
    elif len(items) == 1:
        return items[0]
    elif len(items) == 2:
        return " and ".join(items)
    else:
        return ", ".join(items[:-1]) + " and " + items[-1]

# Examples
print(natural_enumeration(["apples"]))
print(natural_enumeration(["apples", "bananas"]))
print(natural_enumeration(["apples", "bananas", "pears"]))
print(natural_enumeration(["apples", "bananas", "pears", "kiwi"]))
