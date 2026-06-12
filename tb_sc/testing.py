# Sortér etter det andre elementet i hver underliste
data = [[1, 'banana'], [2, 'apple'], [3, 'cherry']]

def second(item):
    return item[1]

print(sorted(data, key=second))
# Alternativ: print(sorted(data, key=lambda x: x[1]))
