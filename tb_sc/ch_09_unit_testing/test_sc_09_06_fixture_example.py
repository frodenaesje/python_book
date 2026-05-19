# file: test_sc_09_06_fixture_example.py
import pytest

class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount

@pytest.fixture
def account():
    return BankAccount(balance=1000)  # kjøres for hver test som ber om "account"

def test_deposit(account):
    account.deposit(500)
    assert account.balance == 1500

def test_withdraw(account):
    account.withdraw(300)
    assert account.balance == 700

def test_overdraw(account):
    with pytest.raises(ValueError):
        account.withdraw(2000)
