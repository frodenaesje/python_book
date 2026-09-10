# sc_06_06_mutability.py
def modify_int(x):
    print('Before:', x, '| id:', id(x))
    x = x + 1          # creates NEW int object
    print('After: ', x, '| id:', id(x))

x = 10
modify_int(x)
print('Outside:', x, '| id:', id(x))

# Output:
# Before:  10   | id: 1754625606160
# After:   11   | id: 1754625606192  <- NEW id!
# Outside: 10   | id: 1754625606160  <- unchanged

def modify_str(s):
    s = s + '!'        # creates NEW str object

msg = 'Hello'
modify_str(msg)
print(msg)             # 'Hello' - unchanged