# file: sc_08_12_bool_truthiness.py

class Wallet:
    def __init__(self, money=0):
        self._money = money

    def __bool__(self):
        return self._money > 0

w1 = Wallet(100)
w2 = Wallet(0)

print(bool(w1))   # True
print(bool(w2))   # False

if w1:
    print("You have money!")
if not w2:
    print("Wallet is empty")

# Without __bool__(), objects are always truthy