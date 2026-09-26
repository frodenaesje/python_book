# Team and Player

## Exercise

We will model a sports team and its players with two classes that work
together. A `Player` holds a name, a jersey number and a goal count. A
`Team` has a name and a list of `Player` objects. Most of the work is in
choosing the right operators for a `Team`.

**Player**

Attributes (leading underscore): `_name`, `_number`, `_goals`

- `@property number` - getter and setter. Validate that the number is
  between 1 and 99, and raise a `ValueError` otherwise.
- `@property goals` - getter and setter. Validate that goals are not
  negative, and raise a `ValueError` otherwise.
- `score(n=1)` - add `n` goals. Go through the `goals` setter so the
  validation still applies.
- `__eq__()` - two players are equal if they have the same name and number.
- `__str__()` - e.g. `Ada (#14, 12 goals)`.

The validation (the `raise` statements) is already written in the start file,
since `raise` was introduced in the "raise ValueError" box earlier in the
chapter. You add the assignment that stores a valid value, plus the type hints.

**Team**

Attributes: `_name`, `_players` (a list of `Player` objects)

- `@property name` - getter and setter.
- `@property total_goals` - read-only. The sum of all players' goals.
- `@property top_scorer` - read-only. The player with most goals, or
  `None` if the team is empty.
- `add(player)` - add a `Player` to the team.
- `__len__()` - the number of players.
- `__contains__(player)` - support `player in team`.
- `__getitem__(index)` - support indexing and slicing (`team[0]`, `team[0:2]`).
- `__lt__(other)` - compare teams by `total_goals`, so a list of teams can
  be sorted.
- `__str__()` - the team name, the number of players, and each player on
  its own line.

**Type hints**

Add type hints to every method. Three cases are worth attention:
`list[Player]` for the roster, `Player | None` as the return type of
`top_scorer`, and the forward reference `"Team"` as the return type of
`__lt__`, where the class refers to itself.

**Why is there no `__add__`?** `+` should produce a *new* value and leave its
operands unchanged - that is how numbers, strings and lists behave, and why
`+` suits value objects like `Fraction` and `Vector2D`. A `Team` is
different: it is an *entity* with a lasting identity, so adding a player
changes *the same* team (Norway is still Norway) rather than creating a new
one. Writing that change as `+` would either hide a mutation behind an
operator that looks side-effect free, or force us to hand back a new object
that no longer matches how we think about a team. So the change belongs in
the named method `add()`, and `+` is left out on purpose.

## Example run

```
Team: Norway (3 players)
  Ada (#14, 12 goals)
  Caroline (#9, 7 goals)
  Guro (#20, 3 goals)

Ada in team?   True
Players:       3
team[0]:       Ada (#14, 12 goals)
First two:     [Ada (#14, 12 goals), Caroline (#9, 7 goals)]
Total goals:   22
Top scorer:    Ada (#14, 12 goals)

After Caroline scores 6:
  Total goals: 28
  Top scorer:  Caroline (#9, 13 goals)

Teams ranked by goals:
  Norway: 28
  Sweden: 32
```

## Hint

Let `__init__` assign through the setters (`self.number = number`), not to
`self._number` directly - then the validation runs at construction for
free. For `total_goals`, keep a running total in a `for` loop. For
`top_scorer`, guard the empty team first (return `None`), then loop over the
players and keep the one with the most goals so far. `__getitem__` can just
forward to the list: `return self._players[index]` handles both an integer
and a slice.

## Topics

- Composition: a class that holds a list of another class
- Properties and validation
- Operator overloading for collection-like objects
- Type hints with our own classes

## Assessment criteria

| Criterion | Description | Weight (%) |
|---|---|---:|
| Player properties and construction | Completes the number and goals setters by storing the validated value (the ValueError checks are provided in the start file), and routes __init__ through the setters (self.number = number) so validation also runs at construction, rather than assigning to _number/_goals directly. | 10 |
| Player equality and string form | Implements __eq__ (equal when name and number match) and __str__ producing output such as 'Ada (#14, 12 goals)'. score(n) adds goals through the goals setter rather than touching _goals directly. | 15 |
| Team as a collection | Team stores a list of Player objects and implements __len__, __contains__, and __getitem__ so that len(team), 'player in team', team[i] and slicing team[i:j] all work. | 25 |
| Team computed properties | Implements total_goals (sum of every player's goals) and top_scorer (the player with most goals, or None for an empty team) as read-only properties, handling the empty-team case correctly. | 25 |
| Team comparison and string form | Implements __lt__ comparing teams by total_goals so a list of teams can be sorted, and __str__ listing the team name, player count and each player on its own line. | 10 |
| Type hints | Adds type hints to every method the student writes (only two example signatures are given in the start file), including list[Player] for the roster, Player &#124; None for top_scorer, and the forward reference "Team" where a method refers to its own class. | 15 |
| **Total** | | **100%** |
