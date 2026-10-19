# University Searches with Generators

## Exercise

Extend exercise 10.4, University Hierarchy. Keep the existing classes and
methods unchanged. The supplied files import them from
`ex_10_04_university.py` in the same directory and define a subclass
`SearchableUniversity(University)`. You may use your own completed version
of 10.4 instead.

Add these two generator methods using `yield`:

- `students_with_min_gpa(min_gpa)`: yield each `Student` whose GPA is
  greater than or equal to `min_gpa`. Include `GraduateStudent` objects.
- `matching_members(query)`: yield every member whose name contains
  `query`, ignoring case. An empty query matches every member.

Yield the original objects in insertion order. Do not construct a result list
inside either method. With no matches, iteration must simply produce no values.
Assume valid numeric GPA thresholds. Do not modify the member list or objects
while consuming a generator.

Use the supplied demonstration to:

1. Create a generator for students with GPA at least 3.5. Retrieve its first
   result with `next()`, consume the rest with `list()`, and consume it again.
2. Call the method again to show that a fresh call returns all qualifying students.
3. Search for `"LEE"` and for a name that is absent.
4. Pass a generator expression to `sum()` to total the GPAs of qualifying
   students. Do not create an intermediate list.

Explain briefly when each generator method starts executing, what happens at
`yield`, and why an exhausted generator does not restart even though the
university can be searched again.

## Example run

```text
First match: Alice Johnson
Remaining matches: ['Clara Lee']
Exhausted: []
Fresh search: ['Alice Johnson', 'Clara Lee']
Name matches: ['Clara Lee']
No matches: []
GPA total: 7.7
```

## Hints

- `isinstance(member, Student)` includes subclasses.
- A generator function ends normally when there are no more matches.
- `list()` in the client demonstration is allowed; it makes results visible.

## Topics

- Generator methods and suspended execution
- Filtering polymorphic collections
- Generator expressions and one-shot consumption

## Assessment criteria

| Criterion | Description | Weight (%) |
|---|---|---:|
| Student generator | Yields students meeting the inclusive GPA threshold, including graduate students, in insertion order. | 30 |
| Name-search generator | Yields all case-insensitive partial name matches and handles no matches. | 30 |
| Generator use | Demonstrates partial consumption, exhaustion, fresh calls, and a generator expression passed to sum. | 25 |
| Explanation | Explains when generator code runs and distinguishes one-shot results from the reusable university. | 15 |
| **Total** | | **100%** |
