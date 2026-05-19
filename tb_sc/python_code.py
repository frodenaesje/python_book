# file: sc_11_05_AccountE_with_exception.py
"""
Enhancing the Account class with custom exceptions for error handling
"""
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
        self.message = message
        self._account_number = account_number
        self._balance = balance
        super().__init__(self.message)
    
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

# Simple bank account with exceptions
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
        print("Dato og tid           | Type     |   Beløp")
        print("-" * 42)
        for trans in self._transactions:
            print(trans)

# Test AccountE with exception handling
if __name__ == "__main__":

    try:
        account1 = AccountE(123, 456, 1000, 2.5)
        account1.deposit(500)
        account1.withdraw(200)
        account1.withdraw(2000)
        account1.add_monthly_interest()
        account1.print_transactions()

        # Use properties
        print(f"\nSaldo etter transaksjoner: {account1.balance:.2f}")
        print(f"Rentesats: {account1.interest}%")

        # Change balance and interest via properties
        account1.balance = 2000
        account1.interest = 3.0
        print(f"\nNy saldo: {account1.balance:.2f}")
    except InsufficientFundsError as e:
        print(f"✗ {e}")
    except NegativeDepositError as e:
        print(f"✗ {e}")
    except BankAccountError as e:
        print(f"✗ Bank error: {e}")
    except Exception as e:
        print(f"✗ Unexpected error: {e}")

    # Simple menu that shows we can continue after errors."
    account2 = AccountE(999, 888, 500, 1.5)
    print("\nMeny: [d]eposit, [w]ithdraw, [s]aldo, [q]uit")
    while True:
        valg = input("Velg: ").strip().lower()
        if valg == "q":
            break
        try:
            if valg == "d":
                belop = float(input("Beløp å sette inn: "))
                account2.deposit(belop)
            elif valg == "w":
                belop = float(input("Beløp å ta ut: "))
                account2.withdraw(belop)
            elif valg == "s":
                pass
            else:
                print("Ukjent valg")
                continue
            print(f"Saldo: {account2.balance:.2f}")
        except (NegativeDepositError, InsufficientFundsError, BankAccountError) as e:
            print(f"✗ {e}")
        except ValueError:
            print("✗ Beløp må være et tall")

print()

