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
sentences = [['Hello', 'there'], ['How', 'are', 'you?']]
for s in sentences:
    print(' '.join(s))
