# Chapter 14 – Answer Key: Review Questions

## Understanding

**1. Two components of a recursive function**
A recursive function must always have a base case — a stopping condition where the function does not make a new recursive call — and a recursive part that makes the problem slightly smaller and calls the function again with this sub-problem. Without a base case the function will call itself indefinitely.

**2. The base case is not necessarily the last call**
The base case only stops further recursive calls in that branch. There may still be many function calls on the call stack waiting to complete on the way back. For Tower of Hanoi with n=3 the base case (n==1) is reached many times — once for each branch in the recursion tree.

**3. Stack frame and memory use**
A stack frame is created for each function call and contains local variables, the return address and temporary state. Recursion uses O(depth) stack memory because each call adds a new frame to the stack — and all of these wait until the base case is reached. Iteration reuses the same frame and uses O(1) extra stack memory.

**4. Linear vs. tree recursion**
Linear recursion has only one recursive call per execution — the call structure is a line. Tree recursion has two or more recursive calls — the call structure branches like a tree. Naive Fibonacci is tree recursion because it calls itself twice.

**5. Tail recursion and Python**
Tail recursion means the recursive call is the absolute last operation — no work happens after it. Python does not have TCO (Tail Call Optimization) and cannot eliminate stack frames for tail calls. Tail recursion therefore gives no advantage in Python, but the concept is important to know since many other languages support it.

**6. Memoisation**
Memoisation means storing previously computed results (typically in a dictionary) and looking them up instead of recomputing. Naive Fibonacci computes the same sub-problems an exponentially large number of times — `fibonacci(3)` is called 2 times, `fibonacci(2)` 3 times, etc. With memoisation each sub-problem is computed exactly once.

**7. Recursion and mathematical induction**
Both build on the idea that a large problem is solved by reducing it to a smaller version of itself. In induction we show that something holds for the base case, and that if it holds for n it holds for n+1. In recursion we implement the base case and the recursive step in the same way. The difference is direction: induction argues forward, recursion runs downward and solves upward.

**8. Step-by-step execution of `countdown(3)`**
```
countdown(3):
  → prints 3
  → calls countdown(2)
      → prints 2
      → calls countdown(1)
          → prints 1
          → calls countdown(0)
              → BASE CASE — prints "Finished!" and returns
          ← returns
      ← returns
  ← returns
```

**9. The stack for `countdown(3)`**
Just before the base case is reached the stack looks like this (top = top of stack):
```
countdown(0)  ← base case
countdown(1)
countdown(2)
countdown(3)  ← first call
```

**10. Why naive Fibonacci is slow**
The same sub-problem is computed many times. `fibonacci(5)` calls `fibonacci(3)` twice, `fibonacci(2)` three times, etc. The number of function calls grows exponentially with n. With memoisation each sub-problem is computed once and looked up directly from the dictionary on repeated calls.

**11. Tower of Hanoi — base case and three steps**
Base case: n == 1 — move the single disk directly. The three steps:
1. Move n-1 disks from SOURCE to HELP (recursively)
2. Move the largest disk from SOURCE to DEST
3. Move n-1 disks from HELP to DEST (recursively)

Step 2 is not the base case — it is the concrete move between the two recursive parts, and can only be performed after step 1 has freed the largest disk.

**12. Recursive directory traversal — base case**
The base case is when `path` points to a file — then the file size is returned directly without further recursive calls. Files are the leaf nodes of the tree structure. When we encounter a directory the recursion continues downward.

**13. When should we not use recursion?**
- When the problem can be solved simply and efficiently with a loop
- When the recursion could go deeper than Python's limit (~1000 levels)
- When performance is critical and function call overhead is a bottleneck
- When the problem does not have a natural "divide-into-smaller-pieces" structure

---

## Practical

**14. Recursive sum of a list**
```python
def sum_list(lst: list[int]) -> int:
    if not lst:        # base case: empty list
        return 0
    return lst[0] + sum_list(lst[1:])

print(sum_list([1, 2, 3, 4, 5]))  # 15
```

**15. Recursive `power(base, exp)`**
```python
def power(base: int, exp: int) -> int:
    if exp == 0:       # base case: x^0 = 1
        return 1
    return base * power(base, exp - 1)

print(power(2, 10))   # 1024
```

**16. Recursive string reversal**
```python
def reverse_string(s: str) -> str:
    if len(s) <= 1:    # base case
        return s
    return reverse_string(s[1:]) + s[0]

print(reverse_string("Python"))  # nohtyP
```

**17. Fibonacci with memoisation**
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
