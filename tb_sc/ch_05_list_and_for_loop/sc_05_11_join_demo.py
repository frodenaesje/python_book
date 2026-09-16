# sc_05_11_join_demo.py

# join() is called on the separator

names = ['Anna', 'Bjorn', 'Clara']
print(', '.join(names))    # Anna, Bjorn, Clara
print(' '.join(names))     # Anna Bjorn Clara
print('-'.join(names))     # Anna-Bjorn-Clara

# All elements must be strings!
numbers = [1, 2, 3, 4]
text = ', '.join([str(n) for n in numbers])
print(text)                # 1, 2, 3, 4

# Build sentences from word lists
sentences = [
    ["Hello", "there", "friend"],
    ["How", "are", "you?"]
]
for s in sentences:
    print(' '.join(s))

def natural_enumeration(items: list) -> str:
    if not items:
        return ""
    elif len(items) == 1:
        return items[0]
    elif len(items) == 2:
        return " and ".join(items)
    else:
        return ", ".join(items[:-1]) + " and " + items[-1]

print(natural_enumeration(["apples"]))
print(natural_enumeration(["apples", "bananas", "pears"]))
