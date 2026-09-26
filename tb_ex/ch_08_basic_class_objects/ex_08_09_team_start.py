# file: ex_08_09_team_start.py
#
# Type hints are part of this exercise. Only a couple of signatures below are
# annotated, as examples of the expected style - add type hints to the rest
# yourself. Watch the three cases from the exercise: list[Player],
# Player | None, and the forward reference "Team".
#
# The number and goals setters are given almost complete, because they use
# raise. A raise stops an invalid value from ever being stored, and it is how
# we say "this is not allowed". You only add the assignment that runs when the
# value is valid - and the type hints.

# TODO: Write the Player class.
#   Attributes (leading underscore): _name, _number, _goals
#   Properties:
#     number, goals - getters are given; each setter validates and then YOU
#                     store the valid value (see the TODO inside the setter)
#   Methods:
#     score(n=1) - add n goals THROUGH the goals setter (so validation runs)
#     __eq__     - equal if same name and number
#     __str__    - e.g. "Ada (#14, 12 goals)"
class Player:
    def __init__(self, name, number, goals=0):
        # Hint: assign _name directly, then use the setters for number and
        # goals (self.number = number) so validation runs at construction too.
        # your code here
        pass

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, value):
        if not 1 <= value <= 99:
            raise ValueError(f"Jersey number {value} must be between 1 and 99")
        # TODO: the value is valid here - store it in self._number
        # your code here

    @property
    def goals(self):
        return self._goals

    @goals.setter
    def goals(self, value):
        if value < 0:
            raise ValueError(f"Goals {value} cannot be negative")
        # TODO: the value is valid here - store it in self._goals
        # your code here

    def score(self, n: int = 1) -> None:      # <- example: signature already typed
        # your code here
        pass

    def __eq__(self, other):
        # your code here
        pass

    def __str__(self):
        # your code here
        pass


# TODO: Write the Team class.
#   Attributes: _name, _players (a list of Player)
#   Properties:
#     name        - getter + setter
#     total_goals - read-only; sum of every player's goals
#     top_scorer  - read-only; the Player with most goals, or None if empty
#   Methods:
#     add(player)          - append a Player
#     __len__              - number of players
#     __contains__(player) - support "player in team"
#     __getitem__(index)   - support team[0] and team[0:2]
#     __lt__(other)        - compare teams by total_goals (for sorting)
#     __str__              - team name, count, then one player per line
class Team:
    def __init__(self, name, players=None):
        # Hint: store the name, and build a NEW list from players so two
        # teams never share the same underlying list.
        # your code here
        pass

    # @property name (getter + setter)
    # your code here

    # @property total_goals (read-only)
    # your code here

    # @property top_scorer (read-only; return None for an empty team)
    # your code here

    def add(self, player):
        # your code here
        pass

    def __len__(self) -> int:                 # <- example: signature already typed
        # your code here
        pass

    def __contains__(self, player):
        # your code here
        pass

    def __getitem__(self, index):
        # your code here
        pass

    def __lt__(self, other):
        # your code here
        pass

    def __str__(self):
        # your code here
        pass


if __name__ == "__main__":
    # TODO: create a few Players, build a Team with add(), then exercise:
    #   printing the team, "player in team", len(team), team[0], slicing,
    #   total_goals, top_scorer, and sorting a list of teams by total_goals.
    pass
