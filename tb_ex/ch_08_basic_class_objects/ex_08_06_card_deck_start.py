# file: ex_08_06_card_deck_start.py
import random

SUITS  = ["Clubs", "Diamonds", "Hearts", "Spades"]
VALUES = ["2", "3", "4", "5", "6", "7", "8", "9", "10",
          "Jack", "Queen", "King", "Ace"]

class Card:
    def __init__(self, suit, value):
        # TODO: store _suit and _value
        pass

    def __str__(self):
        # TODO: return e.g. "Ace of Spades"
        pass

    def __repr__(self):
        return self.__str__()


class Deck:
    def __init__(self):
        # TODO: create all 52 cards using nested loops over SUITS and VALUES
        # Store them in self._cards as a list
        pass

    def shuffle(self):
        # TODO: shuffle _cards in place using random.shuffle
        pass

    def draw(self):
        # TODO: remove and return the top card (index 0)
        # Raise IndexError if the deck is empty
        pass

    def __len__(self):
        # TODO: return number of remaining cards
        pass

    def __getitem__(self, index):
        # TODO: return card at given index
        pass

    def __str__(self):
        # TODO: return e.g. "Deck: 52 cards"
        pass


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
