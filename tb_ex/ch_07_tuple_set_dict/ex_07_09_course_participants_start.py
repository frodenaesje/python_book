# file: ex_07_09_course_participants_start.py

autumn = {
    "Alice Johnson", "Bob Smith", "Charlie Brown",
    "Diana Prince", "Edward Norton", "Fiona Green", "George Harris",
}

spring = {
    "Bob Smith", "Charlie Brown", "Diana Prince",
    "Hannah White", "Ivan Black", "Fiona Green", "Julia Roberts",
}

def print_group(label: str, group: set):
    """Print a group label, count, and sorted members."""
    print(f"\n{label}: {len(group)}")
    for name in sorted(group):
        print(f"  {name}")

# TODO: Find and print all participants (union: autumn | spring)

# TODO: Find and print participants who attended both semesters (intersection: autumn & spring)

# TODO: Find and print participants who dropped out (difference: autumn - spring)

# TODO: Find and print new participants (difference: spring - autumn)

# TODO: Find and print participants who attended exactly one semester
#       (symmetric difference: autumn ^ spring)
