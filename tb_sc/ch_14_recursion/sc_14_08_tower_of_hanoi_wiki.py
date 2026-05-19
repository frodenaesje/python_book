# file: sc_14_08_tower_of_hanoi_wiki.py
# Tower of Hanoi solution based on Wikipedia description
def hanoi(n, source, dest, help):
    if n == 1:
        print(f"Base: Move disk from {source} to {dest}")
    else:
        hanoi(n - 1, source, help, dest)
        print(f"Move disk from {source} to {dest}")
        hanoi(n - 1, help, dest, source)


# Example
print("\nWith 1 disk:")
hanoi(1, "A", "C", "B")
print("\nWith 2 disks:")
hanoi(2, "A", "C", "B")
print("\nWith 3 disks:")
hanoi(3, "A", "C", "B")