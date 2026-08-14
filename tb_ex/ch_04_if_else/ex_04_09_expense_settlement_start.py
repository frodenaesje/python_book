# ex_04_09_expenses_settlement_start.py
# A simplified expense settlement for three friends on a cabin trip.

# Expenses
jonas_paid = 2400    # cabin rental
maria_paid = 950     # food and drinks
simen_paid = 400     # fuel

# --- Part A - Share and balance ---

# TODO: Calculate total, share per person, and the balance for each person

# TODO: Print total, share, and each balance with two decimals


# --- Part B - Status per person ---

# Note: the balances are floating-point numbers. Compare them against a
# small tolerance (for example 0.005), not against == 0, so a tiny
# rounding residual is never mistaken for owing or receiving money.

# TODO: For each person, print whether they should receive, pay, or are settled


# --- Part C - Who pays whom? ---

# A balance is what is still left to settle. One payment goes from a
# debtor (negative balance) to a recipient (positive balance) for
# min(what the debtor owes, what the recipient is owed). After each
# payment, update BOTH balances so later checks use the new state.

# TODO: Write the six possible debtor -> recipient directions as
#       separate if statements (we have no loops yet). In each: check
#       the debtor and recipient against the tolerance, compute the
#       payment with min(), print it, then update both balances.

# TODO: If no one owes anything, print "No payments needed"
