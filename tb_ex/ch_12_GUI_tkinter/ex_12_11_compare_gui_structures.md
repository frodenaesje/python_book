# Compare Four GUI Structures

## Exercise

The same country-list application has been implemented in four ways in the
student source-code directory `tb_sc/ch_12_GUI_with_Tkinter/`:

| Version | File | Structure |
|---|---|---|
| Original | `sc_12_13_entry_list_demo.py` | Nested callback functions |
| v2 | `sc_12_13_entry_list_demo_v2.py` | Standalone functions with global widget variables |
| v3 | `sc_12_13_entry_list_demo_v3.py` | A class with attributes and methods |
| v4 | `sc_12_13_entry_list_demo_v4.py` | Standalone functions with explicit parameters |

Read all four files. If possible, run them separately and try adding a country,
adding a duplicate, submitting an empty entry and removing a selected country.
They are intended to provide the same user-visible behavior.

This is a written comparison task. You do not need to write or modify a program.
Explain the mechanisms in your own words and support your answers with specific
function names, variables or short code excerpts. Listing labels such as
"encapsulation" or "more Pythonic" without explaining their effect is insufficient.
You can complete the task by reading the code if a GUI environment is unavailable.

### 1. Where does the state live?

For each version, explain how `add_country` accesses the entry field, listbox
and status variable. What connects the callback to the particular objects it uses?
Present your answer as a short paragraph per version or a comparison table.

### 2. Why global, but not nonlocal?

In v2, why does `create_gui()` declare three variables as `global`, while
`update_status()` does not need a `global` declaration?

In the original, why can the nested `update_status()` use `status_var` and
`lbx_countries` without declaring them `nonlocal`? Explain the difference between
calling `status_var.set(...)` and assigning a different object to `status_var`.
Would standalone callback functions always require global variables? Use v4
to support your answer.

### 3. Follow one user action

Trace what happens when a user enters a new country and clicks Add, first in
the original and then in v4. Include how the callback receives or finds the
widgets, how the list changes, and how the displayed count is updated.
What is the same about the behavior, and what differs about access to state?

### 4. What does lambda contribute?

Explain this expression from v4:

```python
command=lambda: add_country(en_entry, lbx_countries, status_var)
```

Why would replacing it with the following expression change the behavior?

```python
command=add_country(en_entry, lbx_countries, status_var)
```

### 5. Compare the trade-offs

Give at least one concrete benefit and one concrete drawback of each version.
Consider clarity, repeated argument lists, shared state, the amount of structure,
and how easily a reader can identify a callback's dependencies.
Avoid treating the number of lines as the only measure of simplicity.

### 6. Make and defend a choice

Which version would you choose for each situation, and why?

- A small demonstration intended for students who know functions and scope.
- An application expected to gain several related controls and callbacks.

For each choice, explain one advantage over an alternative and acknowledge
one cost. Is there necessarily one universally "most Pythonic" solution?

## Deliverable

Use `ex_12_11_compare_gui_structures_start.txt` as an answer template.
Submit a written response covering questions 1-6. Use concrete evidence from
the files. Different recommendations are acceptable when the reasoning is
technically correct and fits the stated situation.

## Assessment criteria

| Criterion | Description | Weight (%) |
|---|---|---:|
| State and scope | Explain how all four versions access shared GUI state, including the roles of global, nonlocal and instance attributes. | 35 |
| Callback connections | Trace an Add action and explain deferred calls, parameter passing in version 4. | 30 |
| Comparison and recommendation | Identify a benefit and drawback of each version and justify a recommendation for two different application contexts. | 35 |
| **Total** | | **100%** |
