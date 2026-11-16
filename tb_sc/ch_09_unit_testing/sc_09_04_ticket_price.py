# file: sc_09_04_ticket_price.py

def ticket_price(
    age: int, base_price: float = 160.0
) -> float:
    """Return the ticket price for the given age.

    Under 6: free. 6-17 and 67 or older: half price.
    Others: full price.
    """
    if age < 0:
        raise ValueError(f"Age cannot be negative: {age}")
    if age < 6:
        return 0.0
    if age < 18 or age >= 67:
        return base_price / 2
    return base_price
