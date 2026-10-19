# Help Desk - Iterable, Iterator and Generator

## Exercise

A help desk keeps two lists of ticket descriptions: priority tickets and regular
tickets. To give both queues service, its proposed work schedule alternates
between them, beginning with a priority ticket. When one queue runs out, the
schedule continues through the remaining tickets in the other queue.
Preserve the order within each queue.

Iteration previews the schedule; it does not remove tickets from either list.
Assume that the lists are not changed during a traversal.

1. Implement `HelpDesk(priority, regular)`, storing the two lists.
   Its `__iter__()` must return a new `HelpDeskIterator` each time.
2. Implement `HelpDeskIterator` with `__iter__()` returning itself and
   `__next__()` returning the next ticket according to the scheduling rule.
   Keep iteration progress in the iterator, not in `HelpDesk`.
   Raise `StopIteration` when both queues have been traversed. An exhausted
   iterator must remain exhausted.
3. Implement `GeneratorHelpDesk(priority, regular)` with the same two lists
   and scheduling behaviour. This time, implement `__iter__()` using `yield`,
   without a separate iterator class or an explicit `raise StopIteration`.
   Do not construct a combined list in either version.
4. For each version, use the demonstration in the start file to show that:
   - two traversals of the same help desk produce the full schedule;
   - two iterators over the same help desk progress independently;
   - consuming the rest of one iterator with `list()` leaves it exhausted;
   - either queue may be empty, and both may be empty;
   - neither input list is changed.
5. Explain the difference between the help desk object and an iterator over
   it. Which state does your iterator class store explicitly? Which execution
   state does Python save for the generator?

`list(iterator)` repeatedly requests values until `StopIteration`, consuming
that iterator. A second call on the same exhausted iterator returns `[]`.
By contrast, `list(desk)` calls `iter(desk)` to obtain a fresh iterator, so each
call traverses the full schedule again. A generator-based `__iter__()` also
creates a fresh generator object for each traversal.

## Example schedule

For these lists:

```python
priority = ["Cannot log in", "Server unavailable"]
regular = ["Install a printer", "Update software", "Reset preferences"]
```

Both versions produce this schedule:

```text
Cannot log in
Install a printer
Server unavailable
Update software
Reset preferences
```

## Hints

- Track a position in each list and which queue should have the next turn.
- If the chosen queue is empty or finished, use the other queue.
- Returning a new iterator from `HelpDesk.__iter__()` keeps separate traversals
  independent. Do not reset an existing iterator in its own `__iter__()`.

## Assessment criteria

| Criterion | Description | Weight (%) |
|---|---|---:|
| Iterable and separate iterator | Provides fresh independent iterators that follow the scheduling rule, handle empty queues, and stay exhausted. | 40 |
| Generator version | Uses yield to provide the same reusable traversal without constructing a combined list or changing the queues. | 35 |
| Demonstration and explanation | Demonstrates repeated traversal, independent iterators, exhaustion and boundary cases, and explains where iteration state is stored. | 25 |
| **Total** | | **100%** |
