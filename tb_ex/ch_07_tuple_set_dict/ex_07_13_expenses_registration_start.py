# ex_07_13_expenses_registration_start.py
# Expense settlement with user registered expenses,
# where each expense can apply to only some of the participants.

# --- Provided from ex_07_11 - no changes needed ---

def print_status(balances: dict[str, float]) -> None:
    """Print a status line for each person: receive, pay, or settled."""
    for name, balance in balances.items():
        if balance > 0:
            print(f"{name} should receive {balance:.2f} ")
        elif balance < 0:
            print(f"{name} should pay {-balance:.2f} ")
        else:
            print(f"{name} is settled")


def print_payments(balances: dict[str, float]) -> None:
    """Print the payments that settle all balances.
    Must not modify the dict it receives."""
    balances = balances.copy()   # protect the caller's dict
    payments_made = False
    # Rounding of the shares can leave a residual of a few hundredths on one
    # side only, so we require both a recipient and a debtor above the
    # 0.01 tolerance - otherwise the loop could spin forever.
    while max(balances.values()) > 0.01 and min(balances.values()) < -0.01:
        recipient = max(balances, key=balances.get)
        debtor = min(balances, key=balances.get)
        amount = min(balances[recipient], -balances[debtor])
        print(f"{debtor} pays {amount:.2f} kr to {recipient}")
        balances[recipient] -= amount
        balances[debtor] += amount
        payments_made = True
    if not payments_made:
        print("No payments needed")


# --- Part B - Registration ---

def register_expenses(participants: list[str]) -> list[dict]:
    """Let the user register expenses. Each expense is a dict with the
    keys 'payer', 'amount' and 'participants'."""
    # TODO: Loop until the user enters a blank payer
    # TODO: Validate the payer against the participant list
    # TODO: Read the amount and convert to float
    # TODO: Read the expense participants (blank line = everyone)
    #       and validate every name
    pass


# --- Part C - New balances ---

def calculate_balances(expenses: list[dict],
                       participants: list[str]) -> dict[str, float]:
    """Return a dict with each participant's balance, rounded to two
    decimals. The payer is credited the full amount; each participant
    in the expense is charged an equal share of it."""
    # TODO: Start with balance 0.0 for every participant
    # TODO: Go through the expenses and update the balances
    pass


# --- Part D - Main program ---

# TODO: Ask for the participants (comma separated on one line)

# TODO: Register expenses, calculate balances

# TODO: Print balances, status, and payments