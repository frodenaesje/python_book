# Pythonic patterns – Chapter 8: Classes and objects

## Attribute access — direct vs. property

| Beginner / C++/Java style | Pythonic |
|---------------------------|----------|
| `obj.get_balance()` | `obj.balance` |
| `obj.set_balance(500)` | `obj.balance = 500` |

Properties provide the same interface as plain attributes, but with the option for validation and logic behind the scenes.

## Getter/setter methods vs. property

| Beginner | Pythonic |
|----------|----------|
| `def get_balance(self): return self._balance` | `@property`<br>`def balance(self): return self._balance` |
| `def set_balance(self, v): self._balance = v` | `@balance.setter`<br>`def balance(self, v): self._balance = v` |

Use a property when access should look like ordinary attribute reading. Use an explicit getter method only when the operation is expensive or special (e.g. a database lookup).

## `__str__()` — printing objects

| Beginner | Pythonic |
|----------|----------|
| `def show(self): print(self._name)` | `def __str__(self): return self._name` |
| `obj.show()` | `print(obj)` |

`__str__()` is called implicitly by `print()` and `str()`. No need to remember to call a separate display method.

## Comparing objects

| Beginner | Pythonic |
|----------|----------|
| `def is_equal(self, other): return self._r == other._r` | `def __eq__(self, other): return self._r == other._r` |
| `if c1.is_equal(c2):` | `if c1 == c2:` |

Implement dunder methods for comparison so that objects can be used with standard operators.

## Calling class methods

| Beginner | Pythonic |
|----------|----------|
| `acc1.get_account_count()` | `Account.get_account_count()` |

Call class methods via the class, not via an object. This makes it clear that the method belongs to the class, not the instance.

## Truthiness — checking whether an object is "empty"

| Beginner | Pythonic |
|----------|----------|
| `if wallet.has_money():` | `if wallet:` |
| `if basket.is_empty() == False:` | `if basket:` |
| `if len(basket.items) > 0:` | `if basket:` |

Implement `__bool__()` so that objects can be used directly in `if` expressions without calling an explicit check method.

## Indexing custom collection classes

| Beginner | Pythonic |
|----------|----------|
| `playlist.get_song(0)` | `playlist[0]` |
| `playlist.get_songs(0, 2)` | `playlist[0:2]` |
| `playlist.contains("Song A")` | `"Song A" in playlist` |

Implement `__getitem__()` and `__contains__()` so that custom collection classes behave like built-in sequences.
