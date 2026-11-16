# file: sc_06_16_twelve_days.py
# Traditional song: The Twelve Days of Christmas (public domain).
ORDINALS = [
    "first", "second", "third", "fourth", "fifth", "sixth",
    "seventh", "eighth", "ninth", "tenth", "eleventh", "twelfth"
]
GIFTS = [
    "A partridge in a pear tree.",
    "Two turtle doves,",
    "Three French hens,",
    "Four calling birds,",
    "Five gold rings,",
    "Six geese a-laying,",
    "Seven swans a-swimming,",
    "Eight maids a-milking,",
    "Nine ladies dancing,",
    "Ten lords a-leaping,",
    "Eleven pipers piping,",
    "Twelve drummers drumming,"
]


def print_verse(day: int) -> None:
    """Print one verse; day must be between 1 and 12."""
    print(f"On the {ORDINALS[day - 1]} day of Christmas")
    print("my true love sent to me:")
    for index in range(day - 1, 0, -1):
        print(GIFTS[index])
    if day == 1:
        print(GIFTS[0])
    else:
        print("And " + GIFTS[0].lower())
    print()


if __name__ == "__main__":
    for day in range(1, 13):
        print_verse(day)
