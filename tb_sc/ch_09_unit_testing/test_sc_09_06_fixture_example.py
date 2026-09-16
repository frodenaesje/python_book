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
    return BankAccount(balance=1000)  # runs for each test that requests "account"

def test_deposit(account):
    account.deposit(500)
    assert account.balance == 1500

def test_withdraw(account):
    account.withdraw(300)
    assert account.balance == 700

def test_overdraw(account):
    with pytest.raises(ValueError):
        account.withdraw(2000)


class DataProcessor:
    def __init__(self, data):
        self.data = data

    def count_items(self):
        return len(self.data)

    def has_item(self, item):
        return item in self.data


# scope="module" - created once for the entire file
@pytest.fixture(scope="module")
def processor():
    return DataProcessor(["apple", "banana", "cherry"])


def test_count(processor):
    assert processor.count_items() == 3


def test_has_apple(processor):
    assert processor.has_item("apple") is True


def test_has_orange(processor):
    assert processor.has_item("orange") is False
