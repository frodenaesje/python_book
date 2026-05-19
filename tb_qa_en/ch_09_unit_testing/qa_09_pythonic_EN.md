# Pythonic patterns – Chapter 9: Unit testing

## Test function names

| Beginner | Pythonic |
|----------|----------|
| `def test1():` | `def test_addition_returns_correct_sum():` |
| `def test_a():` | `def test_withdraw_raises_on_insufficient_funds():` |

The test name should say what is being tested and what is expected — then we can see immediately what failed without reading the code.

## Many test values — loop vs. parametrize

| Beginner | Pythonic |
|----------|----------|
| `for year, expected in test_data:` | `@pytest.mark.parametrize("year, expected", [` |
| `    assert is_leap_year(year) == expected` | `    (2000, True), (1900, False), ...` |
| | `])` |
| | `def test_is_leap_year(year, expected):` |
| | `    assert is_leap_year(year) == expected` |

With a loop the test stops at the first failure. With `@pytest.mark.parametrize` all combinations run and we get one error message per failing value.

## Setup in each test function vs. fixture

| Beginner | Pythonic |
|----------|----------|
| `def test_deposit():` | `@pytest.fixture` |
| `    acc = BankAccount(1000)` | `def account():` |
| `    acc.deposit(500)` | `    return BankAccount(1000)` |
| `    ...` | |
| `def test_withdraw():` | `def test_deposit(account):` |
| `    acc = BankAccount(1000)` | `    account.deposit(500)` |
| `    acc.withdraw(300)` | `    ...` |
| `    ...` | `def test_withdraw(account):` |
| | `    account.withdraw(300)` |
| | `    ...` |

A fixture removes duplication and ensures all tests start from the same state.

## Testing exceptions

| Beginner | Pythonic |
|----------|----------|
| `try:` | `with pytest.raises(ValueError):` |
| `    account.withdraw(9999)` | `    account.withdraw(9999)` |
| `except ValueError:` | |
| `    pass` | |

`pytest.raises()` as a context manager is shorter, more readable, and automatically fails if the exception is not raised.

## The AAA pattern

| Without structure | With AAA |
|-------------------|---------|
| `def test_deposit(account):` | `def test_deposit(account):` |
| `    account.deposit(500)` | `    # Arrange — handled by fixture` |
| `    x = account.balance` | `    # Act` |
| `    assert x == 1500` | `    account.deposit(500)` |
| | `    # Assert` |
| | `    assert account.balance == 1500` |

Arrange-Act-Assert makes the test easier to read and debug. When a fixture handles the Arrange step we only need to comment Act and Assert.
