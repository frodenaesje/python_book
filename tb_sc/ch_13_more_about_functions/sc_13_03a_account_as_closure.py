# file: sc_13_03a_account_as_closure.py
# Closure with several functions
def make_account(initial_balance: float = 0):
    """Create a bank account object with a closure."""
    balance = initial_balance  # Private variable
    
    def deposit(amount: float):
        nonlocal balance
        balance += amount
        return balance
    
    def withdraw(amount: float):
        nonlocal balance
        if amount > balance:
            print("Insufficient funds!")
            return balance
        balance -= amount
        return balance
    
    def get_balance():
        return balance
    
    # Return the functions directly as a tuple.
    return deposit, withdraw, get_balance

# Use account: unpack the functions.
deposit, withdraw, get_balance = make_account(1000)
print("\n--- Bank Account Example ---")
print(f"Initial balance: {get_balance()}")
print(f"After deposit 500: {deposit(500)}")
print(f"After withdraw 200: {withdraw(200)}")
print(f"Final balance: {get_balance()}")

# Try to withdraw too much.
withdraw(2000)
