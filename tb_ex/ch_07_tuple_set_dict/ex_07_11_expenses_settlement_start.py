# ex_07_11_expenses_settlement_start.py
# Expense settlement for any number of people.

expenses = {
    "Jonas": 2400.0,    # cabin rental
    "Maria": 950.0,     # food and drinks
    "Simen": 400.0,     # fuel
    "Nora": 0.0,        # came along, paid for nothing
}


def calculate_balances(expenses: dict[str, float]) -> dict[str, float]:
    """Return a new dict with each person's balance (paid - share),
    rounded to two decimals."""
    # TODO: Calculate total and share, build and return the balance dict
    pass


def print_status(balances: dict[str, float]) -> None:
    """Print a status line for each person: receive, pay, or settled."""
    # TODO: Loop over the balances with if-elif-else
    pass


def print_payments(balances: dict[str, float]) -> None:
    """Print the payments that settle all balances.
    Must not modify the dict it receives."""
    # TODO: Work on a copy of balances
    # TODO: Repeat until no balance is greater than 0.01:
    #       find biggest recipient and biggest debtor,
    #       pay the smaller of the two amounts, update both balances
    # TODO: If no payments were needed, print "No payments needed"
    pass


# --- Main program ---

# TODO: Print total and share per person with two decimals

# TODO: Calculate the balances and print each with sign and two decimals

# TODO: Print status lines (part B) and payments (part C)