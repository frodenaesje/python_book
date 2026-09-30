# Chapter 9 – Answer Key: Review Questions

## Understanding

**1. pytest vs. assert in REPL - and naming conventions**
In the REPL, a failed assertion raises `AssertionError` and ends the current evaluation; the REPL remains available for further input. A bare assertion gives a traceback and any supplied message, while pytest provides richer failure reports with inspected values. In a normal run, pytest runs the collected tests and reports which failed, and the suite can be rerun after each code change. The naming conventions used in this chapter are that test filenames and test function names start with `test_`. These allow normal pytest discovery; they are not the only supported naming patterns.

**2. Reading the failure output**
`FAILED test_calc.py::test_addition - AssertionError: assert 5 == 6` means: the test function `test_addition` in the file `test_calc.py` failed. `assert 5 == 6` shows that the function returned 5 but we expected 6.

**3. `@pytest.mark.parametrize` vs. an ordinary loop**
With an ordinary loop the test stops at the first failure — the remaining values are never run. With `@pytest.mark.parametrize` all combinations are run and we get one separate error message per failing value.

**4. `@pytest.fixture`**
`@pytest.fixture` marks a function that provides reusable setup, such as test data and objects. A test requests the fixture by using its name in the parameter list. Before running the test, pytest calls the fixture function as needed and supplies its returned value to that parameter; fixture scope determines when an existing value is reused.

**5. Default scope vs. `scope="module"`**
The default scope (function) creates the fixture fresh before each test function — safe when tests can modify the data. `scope="module"` creates it once for the entire test file — used when resources are expensive to create and tests do not modify them.

**6. The AAA pattern**
Arrange (set up test data and environment), Act (call the function being tested), Assert (check the result). A fixture corresponds to the Arrange step.

**7. Test coverage and its limits**
Coverage measures which parts of the code were executed during testing. 100% line coverage means that every measured executable line ran. It does not mean that every path, branch, input value or edge case was tested, or that the results were correct. Tests can achieve full line coverage without uncovering real bugs.

**8. `pytest.approx()`**
Used to compare floating-point numbers with a permitted deviation. `abs=0.001` means the values may differ by up to 0.001 and the test will still pass.

**9. Avoid logic in tests**
If a test contains `if` statements or loops, the test logic itself can contain errors — and then we do not know whether it is the code or the test that is wrong. Tests should be so simple that they are obviously correct.

**10. `pytest.raises()`**
`with pytest.raises(ValueError):` sets up a trap for `ValueError`. If the code in the block does not raise any exception — or raises the wrong type — the test fails.

---

## Practical

**11. `is_positive()` with `assert`**
```python
def is_positive(n: int) -> bool:
    return n > 0

assert is_positive(5)  == True
assert is_positive(0)  == False
assert is_positive(-3) == False
```

**12. Test file for `is_positive()`**
```python
from my_module import is_positive

def test_positive_number():
    assert is_positive(5) == True

def test_zero_is_not_positive():
    assert is_positive(0) == False

def test_negative_number():
    assert is_positive(-3) == False
```

**13. `celsius_to_fahrenheit` with `pytest.approx()`**
```python
import pytest

def celsius_to_fahrenheit(c: float) -> float:
    return c * 9 / 5 + 32

def test_freezing():
    assert celsius_to_fahrenheit(0) == pytest.approx(32.0, abs=0.1)

def test_boiling():
    assert celsius_to_fahrenheit(100) == pytest.approx(212.0, abs=0.1)

def test_body_temp():
    assert celsius_to_fahrenheit(37) == pytest.approx(98.6, abs=0.1)
```

**14. Parametrised test for `is_positive()`**
```python
import pytest

@pytest.mark.parametrize("value, expected", [
    (-5, False),
    (0,  False),
    (5,  True),
])
def test_is_positive(value, expected):
    assert is_positive(value) == expected
```

**15. `Counter` with fixture**
```python
import pytest

class Counter:
    def __init__(self) -> None:
        self._value = 0

    def increment(self) -> None:
        self._value += 1

    def reset(self) -> None:
        self._value = 0

    def get_value(self) -> int:
        return self._value

@pytest.fixture
def counter() -> Counter:
    return Counter()

def test_initial_value(counter):
    assert counter.get_value() == 0

def test_increment(counter):
    counter.increment()
    counter.increment()
    assert counter.get_value() == 2

def test_reset(counter):
    counter.increment()
    counter.reset()
    assert counter.get_value() == 0
```

**16. `assert "python" == "Python"`**
Raises `AssertionError` because Python is case-sensitive — `"python"` and `"Python"` are not equal strings.

**17. The `Miss` column in coverage**
Save the complete QA13 code, including `celsius_to_fahrenheit()` and its three tests, as `test_temperature.py` in a working folder. From that folder, with pytest and pytest-cov installed, run:

```text
python -m pytest test_temperature.py --cov=test_temperature --cov-report=term-missing
```

Here `test_temperature` is the module being measured. Because this answer keeps the function and tests in one file, the report covers both. `Stmts` counts measured executable statements, `Miss` counts those not executed, and `Cover` gives the percentage executed. Any missed line numbers appear under `Missing`. A successful run of these three tests should exercise every measured line in this small file, giving `Miss` 0 and 100% line coverage. This does not prove correctness for every possible temperature.
