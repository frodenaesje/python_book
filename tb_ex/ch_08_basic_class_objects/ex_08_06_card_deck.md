---
title: "Card Deck"
id: "ex_08_06_card_deck"
tags: ["class", "__len__", "__getitem__", "__str__", "composition", "random"]
difficulty: "medium"
prerequisites: ["class", "__init__", "__len__", "__getitem__", "list", "random"]
learning_outcomes:
  - "Design two collaborating classes (Card and Deck)"
  - "Implement __getitem__ to support indexing"
  - "Use composition - Deck contains Card objects"
  - "Implement shuffle and draw operations"
---

# Card Deck

## Exercise

Create two classes: `Card` and `Deck`.

### Card

**Attributes:** `_suit`, `_value`

**Methods:**
- `__str__()` - e.g. `Ace of Spades`, `10 of Hearts`
- `__repr__()` - same as `__str__`

### Deck

Represents a standard 52-card deck.

**Methods:**
- `__init__()` - create all 52 cards automatically
- `shuffle()` - shuffle the deck using `random.shuffle`
- `draw()` - remove and return the top card. Raise `IndexError` if empty.
- `__len__()` - number of remaining cards
- `__getitem__(index)` - support indexing: `deck[0]`
- `__str__()` - show how many cards remain

Use these suits and values:
```python
SUITS  = ["Clubs", "Diamonds", "Hearts", "Spades"]
VALUES = ["2", "3", "4", "5", "6", "7", "8", "9", "10",
          "Jack", "Queen", "King", "Ace"]
```

## Example run

```
New deck: 52 cards
Top card: 2 of Clubs
deck[0]:  2 of Clubs

After shuffle - top 5 cards:
  King of Hearts
  7 of Diamonds
  3 of Spades
  Ace of Clubs
  10 of Hearts

Drawing 3 cards: King of Hearts, 7 of Diamonds, 3 of Spades
Cards remaining: 49
```

## Topics

- Two collaborating classes
- `__getitem__` for indexing
- `__len__` for `len()`
- Composition: Deck contains Card objects

---
## Instructor notes

**Learning objectives covered:** composition, __len__, __getitem__, two classes

**__getitem__ enables:** Once `__getitem__` is defined, iteration with
`for card in deck` also works automatically - Python calls `__getitem__`
with increasing indices until `IndexError`. Worth demonstrating.

**Extension:** Deal a hand of 5 cards and evaluate whether it contains
a pair, two pairs, etc. (poker hand evaluation).
