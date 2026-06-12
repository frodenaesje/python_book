# file: ex_08_06_card_deck.py
import random

SUITS  = ["Clubs", "Diamonds", "Hearts", "Spades"]
VALUES = ["2", "3", "4", "5", "6", "7", "8", "9", "10",
          "Jack", "Queen", "King", "Ace"]

class Card:
    def __init__(self, suit, value):
        self._suit  = suit
        self._value = value

    def __str__(self):
        return f"{self._value} of {self._suit}"

    def __repr__(self):
        return self.__str__()


class Deck:
    def __init__(self):
        self._cards = [Card(suit, value) for suit in SUITS for value in VALUES]

    def shuffle(self):
        random.shuffle(self._cards)

    def draw(self):
        if not self._cards:
            raise IndexError("The deck is empty.")
        return self._cards.pop(0)

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, index):
        return self._cards[index]

    def __str__(self):
        return f"Deck: {len(self)} cards"


if __name__ == "__main__":
    deck = Deck()
    print(f"New deck: {deck}")
    print(f"Top card: {deck[0]}")
    print(f"deck[0]:  {deck[0]}")

    deck.shuffle()
    print(f"\nAfter shuffle - top 5 cards:")
    for i in range(5):
        print(f"  {deck[i]}")

    print(f"\nDrawing 3 cards: ", end="")
    drawn = [str(deck.draw()) for _ in range(3)]
    print(", ".join(drawn))
    print(f"Cards remaining: {len(deck)}")
