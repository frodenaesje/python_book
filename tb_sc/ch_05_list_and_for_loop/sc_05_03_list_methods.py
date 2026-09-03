# file: sc_05_03_list_methods.py
shopping_list = ['milk', 'bread', 'cheese']
print(shopping_list)                    # ['milk', 'bread', 'cheese']

shopping_list.append('butter')          # add to end
print(shopping_list)                    # ['milk', 'bread', 'cheese', 'butter']

shopping_list.insert(1, 'egg')          # insert at position
print(shopping_list)                    # ['milk', 'egg', 'bread', 'cheese', 'butter']

shopping_list.remove('bread')           # remove first occurrence
print(shopping_list)                    # ['milk', 'egg', 'cheese', 'butter']

last = shopping_list.pop()              # remove + return last
print(last)                             # butter
print(shopping_list)                    # ['milk', 'egg', 'cheese']

pos = shopping_list.index('egg')        # find position
print(pos)                              # 1

shopping_list.append('milk')
cnt = shopping_list.count('milk')       # count occurrences
print(cnt)                              # 2

result = shopping_list.sort()           # sort in place
print(shopping_list)                    # ['cheese', 'egg', 'milk', 'milk']
print(result)                           # None  <- sort() returns None

shopping_list.reverse()                 # reverse in place
print(shopping_list)                    # ['milk', 'milk', 'egg', 'cheese']

shopping_list.extend(['apple', 'juice'])   # add many
print(shopping_list)                    # ['milk', 'milk', 'egg', 'cheese', 'apple', 'juice']

shopping_list.clear()                   # empty the list
print(shopping_list)                    # []