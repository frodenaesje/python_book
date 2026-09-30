# Chapter 14 – Answer Key: Review Questions

## Understanding

**1. Two components of a recursive function**
A terminating recursive solution over its intended input domain needs a reachable base case that handles a result without further recursive calls, and a recursive case for larger instances that makes progress toward a stopping case. Without a reachable stopping case or progress toward it, recursive calls do not terminate normally and may eventually raise `RecursionError`. Without a recursive case, the function may solve only the directly handled case rather than larger instances recursively.

**2. The base case is not necessarily the last call**
The base case only stops further recursive calls in that branch. There may still be many function calls on the call stack waiting to complete on the way back. For Tower of Hanoi with n=3 the base case (n==1) is reached many times — once for each branch in the recursion tree.

**3. Stack frame and memory use**
Each active function call has its own execution frame, including local bindings and information about where execution resumes. The chapter's simple recursive examples keep a chain of active calls while their simple loop-based equivalents reuse one function frame. This adds call-frame overhead. It does not mean that iteration uses no frame, that all Python locals physically occupy a machine stack, or that every recursive solution uses more total memory than every iterative solution.

**4. Linear vs. tree recursion**
Linear recursion makes at most one recursive call from each invocation; a base-case invocation may make none. `countdown` is a linear example. Tree recursion can make multiple recursive calls from one invocation, producing a branching call structure. Naive Fibonacci is an example because each non-base invocation calls both `fibonacci(n - 1)` and `fibonacci(n - 2)`. The distinction concerns calls made by an invocation, not merely the number of textual call sites.

**5. Tail recursion and Python**
In tail recursion, the recursive call is in tail position: its result is returned without pending work that must combine it afterward. CPython does not eliminate Python-function tail-call frames, so tail recursion does not avoid its recursion-depth limit. CPython 3.14's optional internal tail-call interpreter is a different mechanism; it does not provide tail-call optimization of Python functions.

**6. Memoisation**
Memoisation stores computed results, typically in a dictionary, for reuse. Naive Fibonacci repeatedly solves overlapping subproblems: during `fibonacci(5)`, `fibonacci(3)` is called twice and `fibonacci(2)` three times. In the chapter's dictionary implementation, each stored non-base subproblem is expanded once per shared memo dictionary. Calls that find a stored value still occur, but return the cached result. The uncached base cases can still be reached more than once.

**7. Recursion and mathematical induction**
The directly solved recursive base case corresponds to the induction base case. Assuming a smaller subproblem is solved correctly and using its result to construct the larger result corresponds to the induction step. Mathematical induction is a proof method; recursion is an algorithmic/programming technique. A recursive solution also needs progress toward a terminating case; the analogy with induction does not itself guarantee termination.

**Worked example - tracing countdown(3)**
```
countdown(3):
  → prints 3
  → calls countdown(2)
      → prints 2
      → calls countdown(1)
          → prints 1
          → calls countdown(0)
              → BASE CASE - prints "Finished!" and returns
          ← returns
      ← returns
  ← returns
```

**8. The stack for `countdown(3)`**
Just before the base case is reached the stack looks like this (top = top of stack):
```
countdown(0)  ← base case
countdown(1)
countdown(2)
countdown(3)  ← first call
```

**9. Why naive Fibonacci is slow**
The `n - 1` and `n - 2` branches overlap, so the same subproblem is computed repeatedly. During `fibonacci(5)`, `fibonacci(3)` is called twice and `fibonacci(2)` three times. The number of calls grows exponentially with n in this naive algorithm. With the chapter's memoisation implementation, stored non-base computations are reused. Cache-hit calls still happen, and uncached base cases may recur.

**10. Tower of Hanoi - base case and three steps**
Base case: n == 1 — move the single disk directly. The three steps:
1. Move n-1 disks from SOURCE to HELP (recursively)
2. Move the largest disk from SOURCE to DEST
3. Move n-1 disks from HELP to DEST (recursively)

Step 2 is not the base case — it is the concrete move between the two recursive parts, and can only be performed after step 1 has freed the largest disk.

**11. Recursive directory traversal - base case**
When `path` points to a file, `get_size` returns its size directly without recursive calls. An empty directory also terminates descent because it has no children; `sum()` over no child results returns 0. A nonempty directory applies the same operation to each child and combines their results. Recursion fits naturally because directories and their children form a tree-like recursive structure.

**12. When should we not use recursion?**
- When the problem can be solved simply and efficiently with a loop
- When recursion could exceed the current recursion limit, inspectable with `sys.getrecursionlimit()`
- When performance is critical and function call overhead is a bottleneck
- When the problem does not have a natural "divide-into-smaller-pieces" structure

---

## Practical

**13. Recursive sum of a list**
```python
def sum_list(lst: list[int]) -> int:
    if not lst:        # base case: empty list
        return 0
    return lst[0] + sum_list(lst[1:])

print(sum_list([1, 2, 3, 4, 5]))  # 15
```

**14. Recursive `power(base, exp)`**
The intended domain is a non-negative integer `exp`.

```python
def power(base: int, exp: int) -> int:
    if exp == 0:       # base case: x^0 = 1
        return 1
    return base * power(base, exp - 1)

print(power(2, 10))   # 1024
```

**15. Recursive string reversal**
```python
def reverse_string(s: str) -> str:
    if len(s) <= 1:    # base case
        return s
    return reverse_string(s[1:]) + s[0]

print(reverse_string("Python"))  # nohtyP
```

**16. Fibonacci with memoisation**
```python
def fibonacci_memo(n: int, memo: dict | None = None) -> int:
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    return memo[n]

print(fibonacci_memo(10))   # 55
print(fibonacci_memo(50))   # 12586269025
```
