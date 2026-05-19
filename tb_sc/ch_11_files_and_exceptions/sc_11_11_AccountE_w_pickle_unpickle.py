# file: sc_11_11_AccountE_w_pickle_unpickle.py
"""
AccountE with pickle/unpickle functionality for saving and loading accounts
"""
import pickle
from pathlib import Path
from datetime import datetime


class Transaction:
    def __init__(self, amount, trans_type):
        self._amount = amount
        self._trans_type = trans_type  # "deposit", "withdraw", "interest"
        self._timestamp = datetime.now()

    def __str__(self):
        return f"{self._timestamp:%Y-%m-%d %H:%M:%S} | {self._trans_type.capitalize():8} | {self._amount:8.2f}"


class BankAccountError(Exception):
    """Base exception for bank account operations"""
    
    def __init__(self, message, account_number=None, balance=None):
        super().__init__(message)
        self._account_number = account_number
        self._balance = balance
    
    @property
    def message(self):
        return self.args[0] if self.args else ""
    
    def __str__(self):
        base_msg = self.message
        if self._account_number:
            base_msg += f" (Account: {self._account_number})"
        if self._balance is not None:
            base_msg += f" (Balance: ${self._balance:.2f})"
        return base_msg


class NegativeDepositError(BankAccountError):
    """Raised when trying to deposit a negative amount"""
    pass


class InsufficientFundsError(BankAccountError):
    """Raised when trying to withdraw more than the current balance"""
    pass


class AccountE:
    """Bank account that raises exceptions for invalid operations"""
    
    def __init__(self, cust_id, account_no, start_balance, interest=0.0):
        self._cust_id = cust_id
        self._account_no = account_no
        self._balance = start_balance
        self._interest = interest
        self._transactions = []

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, new_balance):
        if new_balance < 0:
            raise BankAccountError(
                "Balance cannot be negative",
                self._account_no,
                self._balance
            )
        self._balance = new_balance

    @property
    def interest(self):
        return self._interest

    @interest.setter
    def interest(self, new_interest):
        if new_interest < 0:
            raise BankAccountError(
                "Interest rate cannot be negative",
                self._account_no,
                self._balance
            )
        self._interest = new_interest

    @property
    def account_no(self):
        return self._account_no

    def deposit(self, amount):
        if amount <= 0:
            raise NegativeDepositError(
                "Deposit amount must be positive",
                self._account_no,
                self._balance
            )
        self._balance += amount
        self._transactions.append(Transaction(amount, "deposit"))
        return self._balance

    def withdraw(self, amount):
        if amount > self._balance:
            raise InsufficientFundsError(
                f"Cannot withdraw ${amount:.2f}",
                self._account_no,
                self._balance
            )
        self._balance -= amount
        self._transactions.append(Transaction(amount, "withdraw"))
        return self._balance

    def add_monthly_interest(self):
        monthly_interest = self.calculate_monthly_interest()
        self._balance += monthly_interest
        self._transactions.append(Transaction(monthly_interest, "interest"))
        return self._balance

    def calculate_monthly_interest(self):
        return self._balance * self._interest / 100 / 12

    def print_transactions(self):
        print("Date and time         | Type     | Amount")
        print("-" * 42)
        for trans in self._transactions:
            print(trans)
    
    def save_to_file(self, filename):
        """Save account to a binary pickle file"""
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
            print(f"✓ Account {self._account_no} saved to {filename}")
        except Exception as e:
            print(f"✗ Error saving account: {e}")
    
    @staticmethod
    def load_from_file(filename):
        """Load account from a binary pickle file"""
        try:
            with open(filename, 'rb') as f:
                account = pickle.load(f)
            print(f"✓ Account {account.account_no} loaded from {filename}")
            return account
        except FileNotFoundError:
            print(f"✗ File {filename} not found")
            return None
        except Exception as e:
            print(f"✗ Error loading account: {e}")
            return None
    
    def __repr__(self):
        return f"AccountE(cust_id={self._cust_id}, account_no={self._account_no}, balance={self._balance:.2f}, interest={self._interest}%)"


# ========== DEMO: Basic pickle/unpickle ==========

def demo_basic_pickle():
    """Demonstrate basic saving and loading of an account using pickle"""    
    # Create an account with some transactions
    print("\n1. Creating account and performing transactions...")
    account = AccountE(123, 456789, 1000, 2.5)
    account.deposit(500)
    account.withdraw(200)
    account.add_monthly_interest()
    
    print(f"\nOriginal account: {account}")
    print(f"Balance: ${account.balance:.2f}")
    print(f"Number of transactions: {len(account._transactions)}")
    
    # Save to pickle file
    print("\n2. Saving account to pickle file...")
    filename = "account_456789.pkl"
    account.save_to_file(filename)
    
    # Verify file exists
    if Path(filename).exists():
        file_size = Path(filename).stat().st_size
        print(f"   File size: {file_size} bytes")
    
    # Load from pickle file
    print("\n3. Loading account from pickle file...")
    loaded_account = AccountE.load_from_file(filename)
    
    if loaded_account:
        print(f"\nLoaded account: {loaded_account}")
        print(f"Balance: ${loaded_account.balance:.2f}")
        print(f"Number of transactions: {len(loaded_account._transactions)}")
        
        print("\n4. Verifying loaded account works correctly...")
        loaded_account.deposit(100)
        print(f"After deposit of $100: ${loaded_account.balance:.2f}")
        
        print("\n5. Transaction history:")
        loaded_account.print_transactions()


# ========== DEMO: Interactive menu with save/load ==========

def interactive_menu():
    """Interactive menu with save and load functionality"""
    print("\n" + "=" * 60)
    print("INTERACTIVE BANK MENU WITH SAVE/LOAD")
    print("=" * 60)
    
    account = None
    
    print("\nCommands:")
    print("  [n]ew    - Create new account")
    print("  [l]oad   - Load account from file")
    print("  [d]eposit- Deposit money")
    print("  [w]ithdraw- Withdraw money")
    print("  [b]alance- Show balance")
    print("  [t]rans  - Show transactions")
    print("  [i]nterest- Add monthly interest")
    print("  [save]   - Save account to file")
    print("  [q]uit   - Quit")
    
    while True:
        print("\n" + "-" * 60)
        choice = input("Choice: ").strip().lower()
        
        if choice == "q":
            # Offer to save before quitting
            if account:
                save_prompt = input("Save account before quitting? (y/n): ").strip().lower()
                if save_prompt == "y":
                    filename = f"account_{account.account_no}.pkl"
                    account.save_to_file(filename)
            print("Goodbye!")
            break
        
        try:
            if choice == "n":
                # Create new account
                cust_id = int(input("Customer ID: "))
                account_no = int(input("Account number: "))
                start_balance = float(input("Starting balance: "))
                interest = float(input("Interest rate (%): "))
                account = AccountE(cust_id, account_no, start_balance, interest)
                print(f"✓ Account {account_no} created")
            
            elif choice == "l":
                # Load account from file
                account_no = input("Account number to load: ").strip()
                filename = f"account_{account_no}.pkl"
                loaded = AccountE.load_from_file(filename)
                if loaded:
                    account = loaded
            
            elif choice == "d":
                if not account:
                    print("✗ No active account. Create or load an account first.")
                    continue
                amount = float(input("Amount to deposit: "))
                account.deposit(amount)
                print(f"✓ Deposited ${amount:.2f}")
                print(f"  New balance: ${account.balance:.2f}")
            
            elif choice == "w":
                if not account:
                    print("✗ No active account. Create or load an account first.")
                    continue
                amount = float(input("Amount to withdraw: "))
                account.withdraw(amount)
                print(f"✓ Withdrew ${amount:.2f}")
                print(f"  New balance: ${account.balance:.2f}")
            
            elif choice == "b":
                if not account:
                    print("✗ No active account. Create or load an account first.")
                    continue
                print(f"Balance: ${account.balance:.2f}")
                print(f"Interest rate: {account.interest}%")
            
            elif choice == "t":
                if not account:
                    print("✗ No active account. Create or load an account first.")
                    continue
                if account._transactions:
                    account.print_transactions()
                else:
                    print("No transactions yet")
            
            elif choice == "i":
                if not account:
                    print("✗ No active account. Create or load an account first.")
                    continue
                monthly_interest = account.calculate_monthly_interest()
                account.add_monthly_interest()
                print(f"✓ Added monthly interest: ${monthly_interest:.2f}")
                print(f"  New balance: ${account.balance:.2f}")
            
            elif choice == "save":
                if not account:
                    print("✗ No active account. Create or load an account first.")
                    continue
                filename = f"account_{account.account_no}.pkl"
                account.save_to_file(filename)
            
            else:
                print("✗ Unknown command")
        
        except (NegativeDepositError, InsufficientFundsError, BankAccountError) as e:
            print(f"✗ {e}")
        except ValueError as e:
            print(f"✗ Invalid input: {e}")
        except Exception as e:
            print(f"✗ Unexpected error: {e}")


# ========== DEMO: Save and load multiple accounts ==========

def demo_multiple_accounts():
    """Demonstrate saving and loading multiple accounts"""
    print("\n" + "=" * 60)
    print("DEMO: Multiple Accounts")
    print("=" * 60)
    
    # Create multiple accounts
    accounts = [
        AccountE(1, 100, 1000, 2.5),
        AccountE(2, 200, 2500, 3.0),
        AccountE(3, 300, 5000, 3.5)
    ]
    
    # Perform some transactions
    accounts[0].deposit(500)
    accounts[1].withdraw(500)
    accounts[2].add_monthly_interest()
    
    # Save all accounts
    print("\nSaving accounts...")
    for acc in accounts:
        filename = f"account_{acc.account_no}.pkl"
        acc.save_to_file(filename)
    
    # Load all accounts
    print("\nLoading accounts...")
    loaded_accounts = []
    for acc_no in [100, 200, 300]:
        filename = f"account_{acc_no}.pkl"
        loaded = AccountE.load_from_file(filename)
        if loaded:
            loaded_accounts.append(loaded)
    
    # Display loaded accounts
    print("\nLoaded accounts:")
    for acc in loaded_accounts:
        print(f"  Account {acc.account_no}: Balance ${acc.balance:.2f}")


# ========== MAIN ==========

if __name__ == "__main__":
    # Run basic demo
    demo_basic_pickle()
    
    # Run multiple accounts demo
    demo_multiple_accounts()
    
    # Run interactive menu
    run_menu = input("\nRun interactive menu? (y/n): ").strip().lower()
    if run_menu == "y":
        interactive_menu()
    
    print()
